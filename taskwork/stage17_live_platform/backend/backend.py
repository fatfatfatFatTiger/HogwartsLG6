
import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from HogwartsLG6.taskwork.stage17_platform.backend.common.connect_to_db import DB

app = Flask(__name__)
api = Api(app)

uri = DB().connect_db()
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False  # 避免显示中文乱码
db = SQLAlchemy(app)


class Suite(db.Model):
	# 设置保存的表名
	__tablename__ = 't_suites'
	suite_id = db.Column(db.Integer, primary_key=True)
	suite_name = db.Column(db.String(80), unique=False, nullable=False)
	suite_desc = db.Column(db.String(120), unique=False, nullable=True)
	suite_remark = db.Column(db.String(500), unique=False, nullable=True)

	def __repr__(self):
		return json.dumps({
			"suite_id": self.suite_id,
			"suite_name": self.suite_name,
			'suite_desc': self.suite_desc
		}, ensure_ascii=False)


class Case(db.Model):
	# 设置保存的表名
	__tablename__ = 't_cases'
	case_id = db.Column(db.Integer, primary_key=True)
	case_name = db.Column(db.String(80), unique=False, nullable=False)
	case_desc = db.Column(db.String(120), unique=False, nullable=True)
	case_steps = db.Column(db.String(1024), unique=False, nullable=True)
	suite_id = db.Column(db.Integer, db.ForeignKey('t_suites.suite_id'), nullable=False)
	case_remark = db.Column(db.String(500), unique=False, nullable=True)
	suite = db.relationship('Suite', backref=db.backref('case', lazy=True))

	def __repr__(self):
		# 代表要返回类里的一个具体的表现形态，即请求后呈现的格式，如：["<Cases '登录成功'>", "<Cases '登录失败'>", "<Cases '模糊查询'>"]
		# 如果不指定，默认返回第一个字段？
		return json.dumps({
			"case_id": self.case_id,
			"case_name": self.case_name,
			"case_desc": self.case_desc,
			"case_steps": self.case_steps,
			"suite_id": self.suite_id,
			"case_remark": self.case_remark
		}, ensure_ascii=False)

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TestSuiteService(Resource):
	def get(self):
		testsuites = [str(item) for item in Suite.query.all()]
		return jsonify(testsuites)

	def post(self):
		"""
		新增测试用例，使用post来代替put和delete也是很多公司常用的做法
		"""
		app.logger.info(request.args)
		if 'suite_name' not in request.args:
			app.logger.info(request.json)
			# testsuite = Suite(**request.json)
			# app.logger.info(testsuite)
			# db.session.add(testsuite)
			# db.session.commit()
			cst = Suite(**request.json)
			app.logger.info(cst)
			return repr(cst)


class TestCaseService(Resource):
	def get(self):
		"""
		获取所有的接口测试用例或单个测试用例，返回json结构体
		"""
		# 把数据库对象，换一个方法，取出来里面可以打印的部分
		testcases = [str(item) for item in Case.query.all()]
		return jsonify(testcases)

	def post(self):
		"""
		新增测试用例，使用post来代替put和delete也是很多公司常用的做法
		"""
		app.logger.info(request.args)

		if 'case_name' not in request.args:
			app.logger.info(request.json)
			# 此处使用的request是flask里的类，json表示客户端发送过来的form表单json格式或各种格式，
			# 使用request.json把请求体作为整个json结构来进行管理
			# testcase = Case(**request.json)
			# # 把请求中的steps转换成字符串
			# testcase.steps = json.dumps(request.json.get('case_steps'))
			# app.logger.info(testcase)
			# db.session.add(testcase)
			# db.session.commit()
			# return {
			# 	'msg': 'ok',
			# 	'errcode': 0
			# }
			yl = Case(**request.json)
			return yl

	def put(self):
		"""
		修改测试用例，有时候会通过post来代替put
		"""
		app.logger.info(request.args)
		if 'case_name' in request.args:
			Case.query.filter_by(case_name=request.args.get('case_name')).update(request.json)
			db.session.commit()
			return {
				'errcode': 0
			}

	def delete(self):
		"""
		删除特定用例
		"""
		app.logger.info(f"请求参数：{request.args}")
		testcase = Case.query.filter_by(case_name=request.args.get('case_name')).first()
		app.logger.info(testcase)
		db.session.delete(testcase)
		db.session.commit()
		return {
			'errcode': 0
		}


api.add_resource(TestSuiteService, '/testsuite')
api.add_resource(TestCaseService, '/testcase')


def relationship():
	tss = TestSuiteService()
	tcs = TestCaseService()
	cst = tss.post()
	yl = tcs.post()
	cst.case.append(yl)

	db.session.add(cst)
	db.session.commit()


# 直接启动
if __name__ == '__main__':
	app.run(debug=True)

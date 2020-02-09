import time

print(time.strftime("%Y-%m-%d", time.gmtime()))

dic = {'01':{'name':'Сократ', 'surname':'Ясенков', 'patronymic':'Григориевич', 'date':'2002-10-17'},
	'02':{'name':'Адам', 'surname':'Сюкосев', 'patronymic':'Матвеевич', 'date':'2001-02-07'},
	'03':{'name':'Анисья', 'surname':'Карандашова', 'patronymic':'Кузьмевна', 'date':'2001-11-26'},
	'04':{'name':'Артём', 'surname':'Леонидов', 'patronymic':'Игоревич', 'date':'2002-12-15'},
	'05':{'name':'Роза', 'surname':'Угличинина', 'patronymic':'Михеевна', 'date':'2001-01-01'},
	'06':{'name':'Дина', 'surname':'Токмакова', 'patronymic':'Игнатиевна', 'date':'2002-11-26'},
	'07':{'name':'Наталия', 'surname':'Карамзина', 'patronymic':'Феликсовна', 'date':'2002-04-21'},
	'08':{'name':'Алексей', 'surname':'Ажикелямов', 'patronymic':'Гордеевич', 'date':'2002-09-20'},
	'09':{'name':'Таисия', 'surname':'Мишнева', 'patronymic':'Ефимовна', 'date':'2002-02-02'},
	'10':{'name':'Елизавета', 'surname':'Гершельмана', 'patronymic':'Давидовна', 'date':'2001-12-14'}
	}

print(dic)

a = time.strftime("%m-%d", time.gmtime())
for i in dic:
	b = dic[i]['date']
	if b[5:10]==a:
		print(dic[i]['name'],dic[i]['surname'],'Happy Birthday!')

import requests
import json

class Mercury:
	def __init__(self, amount):
		self._amount = amount
		self._authorize_response = 0
		self._json_data_response = ''
		self._cmdStatus_response = ''

	@property
	def authorize_response(self):
		return self._authorize_response

	@property
	def json_data_response(self):
		return self._json_data_response

	@property
	def cmdStatus_response(self):
		return self._cmdStatus_response

	def doCall(self):
		data = {
			'InvoiceNo':'1',
			'RefNo':'1',
			'Memo':'raspberry pi testing',
			'Purchase':round(self._amount,2),
			'Frequency':'OneTime',
			'RecordNo':'RecordNumberRequested',
			'EncryptedFormat':'MagneSafe',
			'AccountSource':'Swiped',
			'EncryptedBlock':'2F8248964608156B2B1745287B44CA90A349905F905514ABE3979D7957F13804705684B1C9D5641C',
			'EncryptedKey':'9500030000040C200026',
			'OperatorID':'test'
		}

		data_json = json.dumps(data)

		print data_json
		print
		print

		headers = {'content-type': 'application/json', 'Authorization':'Basic MDE5NTg4NDY2MzEzOTIyOnh5eg=='}
		r = requests.post("https://w1.mercurycert.net/PaymentsAPI/Credit/Sale", data=data_json, headers=headers)
		self._json_data_response = json.loads(r.text)
		self._authorize_response = self._json_data_response['Authorize']
		self._cmdStatus_response = self._json_data_response['CmdStatus']

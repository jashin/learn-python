import string

form_letter = '''Dear $customer,
blah blah blah
this is your $$5 coupon
Thanks,
$manager
${name}Inn'''

letter_template = string.Template(form_letter)

print letter_template.substitute({'name':'holiday','manager':'steven','customer':'erica silver'})
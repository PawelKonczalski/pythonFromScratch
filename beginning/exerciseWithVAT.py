englishCourseNetPrice = 45
chineseCourseNetPrice = 55
VAT = 23
vatValue = 1 + VAT /100

englishCourseGrossPrice = englishCourseNetPrice * vatValue
chineseCourseGrossPrice = chineseCourseNetPrice * vatValue

print('English course gross price: ',englishCourseGrossPrice, '$')
print('Chinese course gross price: ',chineseCourseGrossPrice, '$')

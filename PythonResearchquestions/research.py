# 1)Listle,tuple,range arasindaki ferqler nelerdir?
# + List-Siyahılar sıralı və dəyişkən kolleksiyalardır. Dublikat xassələrə malikdir (eyni elementdən 2-yə malikdir).[]-bu parametrden
# istifade olunur.
# + Tuple-Tuples sifarişlidir, lakin dəyişməzdir. Dublikat xüsusiyyətlərə malikdir.Tuple- da () sade parantezden istifade edirik.
# Tuple strukturuna elementlər əlavə edilə bilməz, tuple strukturunda elementləri atmaq olmaz.
# + Range-funksiyası daxili funksiyadır, üç müxtəlif parametr var: başlanğıc dəyəri, artım dəyəri və son dəyər
# bu parametrlərə uyğun olaraq tam ədədlər massivi yaradan daxili funksiyadır.
# 2) while ve for dovrleri arasindaki ferqler nelerdir ?
# +For döngəsi proqramçıya müəyyən sayda dəfə yerinə yetirməli olan dövrəni səmərəli şəkildə yazmağa imkan verən təkrar nəzarət strukturudur.
# +İterasiyaların sayı məlum olduqda for loopundan istifadə etmək olar.
# +while döngəsi verilən şərt doğru olduğu müddətcə hədəf ifadələrini yerinə yetirən təkrar idarəetmə quruluşudur.
# +İterasiya sayı naməlum olduqda while dövrəsindən istifadə edilə bilər.Müəyyən bir dövrədə, əgər başlanğıc ifadəsi döngənin içərisindədirsə, dövrə hər dəfə təkrarlananda işə salınır.
# 3)Listlerde append ve insert methodlari arasindaki ferqler nelerdir ?
# + Python append və insert arasında sadə bir fərq var:
# append metodu yalnız siyahıya yeni element əlavə etmək üçün istifadə edilə bilər, lakin insertdən istifadə etməklə biz əlavə edə bilərik, həmçinin artıq işğal olunmuş mövqeyi dəyişdirə bilərik.
# əlavə etmə metodu bir arqument (siyahıya daxil etməlisiniz) götürür, daxil etmə metodu isə iki elementi götürür (əvvəlcə elementin mövqeyi, ikincisi isə elementin özü olacaq).
# 4)List Methodlari hansilardir ?
# -append() metodu Python siyahılarının sonuna element əlavə etmək üçün istifadə olunur.
# -insert() metodu Python siyahılarında göstərilən indeksə element əlavə etmək üçün istifadə olunur.
# -Python siyahılarından elementləri silmək üçün istifadə edə biləcəyimiz müxtəlif üsullar var. Siyahıdan elementi silmək üçün remove() metodundan istifadə edə bilərik.
# -Pop() metodu Python siyahılarında göstərilən indeksdəki elementi silmək üçün istifadə olunur. İndeks nömrəsini göstərməsək, siyahının sonuncu elementi silinir.
# -del() metodu ilə biz istənilən indeks nömrəsinin elementini silə bilərik.Əgər del() metoduna indeks nömrəsi verməsək, o, siyahını olduğu kimi siləcək.
# -Siyahının məzmununu başqa siyahıya təyin etmək üçün copy() metodundan istifadə edə bilərik.
# -Siyahını köçürmək üçün istifadə edə biləcəyimiz başqa bir vasitə list() metodudur.
# -Siyahı elementlərini çeşidləmək üçün sort() metodundan istifadə olunur .
# -Reverse() metodu ilə siyahı elementlərini tərsinə çap edə bilərik.
# -Siyahıda təkrarlanan elementlərin sayını almaq üçün count() metodundan istifadə edirik.
# 5)Scope nedir ?
# -Dəyişənlər sadəcə olaraq məlumatları yaddaşda saxlayan vahidlərdir.  Python-da hər dəyişən və funksiyanın əhatə dairəsi var.  Python hər bir dəyişəni ad məkanında müəyyən edir.
# 6) Pythonda //,% ve ** operatorlarini izah edin.
# - // bu bolme operatorudur ve tam bir eded almaq ucun istifade olunur. % mod alma operatorudur ve qaligi almaq ucun istifade olunur. ** bu ise ededin quvvetini tapmaq ucundur.
# 7) Mentiqi operatorlari izah edin : - Python və operatoru ilə göstərilən şərtlərin hamısı doğrudursa True, ən azı biri yanlışdırsa, False qaytarır.
# -Python və ya operatorla müəyyən edilmiş şərtlərdən yalnız birinin doğru olması nəticənin True olması üçün kifayətdir. Hamısı yalan olarsa, nəticə Yalan olacaq.
# -Python != bu operator ile, şərtlər tərsinə çevrilir. Məsələn, şərt False verirsə, not operatoru ilə True vəziyyətinə çevrilir.
# -1- Daxil edilmiş nömrənin 0-100 arasında olub olmadığını yoxlayın.

#"""nömre = float (giris ( 'nömrə: ' ))
#netice = (nömre > 0 ) and (sayı<= 100 )
#cap (f '0-100 arasında olan ədəddir: {netice}' )


# -2- Daxil edilmiş nömrənin müsbət cüt ədəd olub olmadığını yoxlayın.

#sayı = int (giris ( 'nömre: ' ))
#netice = (ədəd > 0 ) and (sayı % 2 == 0 )
#cap (f 'daxil edilmiş ədəd müsbət cüt ədəddir: {netice}' )

# 8) String in uzunlugunu nece hesablamaq olar ? - Bu zaman biz Lenght methodundan  istifade edirik.(len.String)

# 9) Listden sonuncu elementi nece silmek olar ? - Bu zaman biz print("list.remove(item)") istifade ederik.

# 10) Stringin ilk herfini nece boyuk herfle yazmaq olar ? - Buzaman biz Upper and Slower methodlarindan istifade edirik.

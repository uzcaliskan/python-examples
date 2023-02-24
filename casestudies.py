#CASE STUDY - 1
text = "The goal is to turn data into information, and information into insight."
k = text.replace(","," ").replace("."," ").upper().split() #istenen çıktı

lst1 = "DATASCIENCE"
lst = []
for i in lst1:
    lst.append(i)
[i for i in lst1]
len(lst) #11 elemanlı liste
lst[0] + lst[10]
lst2 = lst[0:4]
lst3 = []
for i in range(4):
    lst3.append(lst[i])
lst.pop(8)  # silinecek index'i yazıoruz!!!
lst.append("new")
lst.insert(8,"N")

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante" : ["Italy", 25]}
dict.keys()
dict.values()
dict["Daisy"][1] = 13
dict["Ahmet"] = ["Turkey", 24]
dict.pop("Antonio")  # value'lar ile birlikte tamamen siliniyor!!

l = [2, 13, 18, 93, 22]

def liste_ayir(dizi):
    cift= []
    tek = []
    for i in dizi:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    return cift, tek

cift_liste, tek_liste = liste_ayir(l)  # aynı anda iki değer alınabiliyor!!

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

muh = []
tip = []

for i, j in enumerate(ogrenciler):
    if i < 3:
        muh.append(j)
    else:
        tip.append(j)
print(muh)

ders_kodu = ["cmp1005", "psy1001", "huk1005", "sen2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

x = zip(ders_kodu, kredi, kontenjan)
list(x)

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lamda", "python", "miuul"])
kume1.difference(kume2)
kume1.intersection(kume2)

def kumeler(kumx, kumy):

    if kumx.issubset(kumy):
        return kumy.difference(kumx)
    else:
        return kumx.intersection(kumy)

def kumeler2(kuma, kumb):
    if kuma.issuperset(kumb):
        return kuma.intersection(kumb)
    else:
        return kuma.difference(kumb)
def kumeler3(kumk, kuml):
    if kumk.issuperset(kuml):
        return kumk.intersection(kuml)
    else:
        return kuml.difference(kumk)

kumeler(kume1, kume2)
kumeler2(kume1, kume2)

def yeni_kume(x1, x2):
    if x1.issuperset(x2):
        return x1.intersection(x2)
    else:
        return x2.differecence(x1)
yeni_kume(kume1, kume2)
kumeler3(kume1, kume2)

#CASE STUDY-2 (BAŞLAMADAN ÖNCE CASE STUDY-1 İN CEVAPLARININ İZLEMEK ÖENMLİ!)
import pandas as pd
import seaborn as sns
import numpy as np
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("car_crashes")
df.head()

df_new = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns ] # df[col].dtype != "O" kısmındaki O harfi mutlaka büyük olmalı!

df_new2 = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
type(df.columns)

og_list = ["abbrev" , "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
#new_cols = [col for col in df.columns if col not in og_list]
new_df3 = df[new_cols]
new_df3.head()

dfx = df.loc[:, (~df.columns.str.contains("abbrev")) & (~df.columns.str.contains("no_previous")) ] #loc ile içinde iki değişken olmayan bu şekilde de seçilebiliyor!
dfy = df.loc[:, (~df.columns.str.contains("abbrev|no_previous" ))] #stckoverflow'dan buldum. bu daha kullanışlı!! ya da(|) işareti çok kullanışlı contains içinde
dfy.head()

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.width",600)
df = sns.load_dataset("car_crashes")
df.head()
og_list = ["abbrev" , "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
df_new = df[new_cols]
df_new.head()

df_new5 = df.loc[:, ~df.columns.str.contains("abbrev|no_previous")]
df_new5.head()

df = sns.load_dataset("titanic")
df.head()
df["sex"].value_counts() # cinsiyet değişkenindeki kategorilernin sayısı(kadın/erkek)
{df[col].name: df[col].nunique() for col in df.columns} #her bir dğeişkenin benzersiz değer sayısı
df.nunique() #tüm değişkenlerin benzersiz değerlerini veriyor. çıktı: pandas serisi'dir.
type(df["pclass"].unique()) #pclass değişkeninin unique değer sayısı !!
{df[col].name:df[col].nunique() for col in df.columns if (df[col].name == "pclass") | (df[col].name == "parch")} # parch ve pclass değişkenlerinin unique sayısı
df.loc[:,["pclass", "parch"]].nunique() # parch ve pclass değişkenlerinin unique sayısı
df[["pclass", "parch"]].nunique() # parch ve pclass değişkenlerinin unique sayısı

df["embarked"] = df["embarked"].astype("category")
df["embarked"] = df["embarked"].astype("O", copy=False)
df.info()

df.loc[df["embarked"] == "C"].head() #embarked C olanları loc ile seçtik
df[df["embarked"] == "C"].head()#embarked C olanları seçtik
df[df["embarked"] != "S"].head() #embarked değeri S olmayanları aldık.
df[df["embarked"] != "S"]["embarked"].unique()#embarked değeri S olmayanları aldık.
df[~(df["embarked"] == "S")]["embarked"].unique() # ~ işaretini kullanmak için fancy index kısmı parantez içinde yazıldı.
df.loc[(df["age"] < 30) & (df["sex"] == "female")] # satır ve sütun aynı anda seçiliğinde özellikle loc kullanmak gerekiyodu!
df[(df["age"] < 30) & (df["sex"] == "female")] # satır ve sütun aynı anda seçilmediğinden bu şkeidle direkt olarak seçim işlemi yapabildik!!
df[(df["fare"] > 500) | (df["age"] > 70)].head()
df.loc[(df["fare"] > 500) | (df["age"] > 70)]

{df[col].name: df[col].isnull().sum() for col in df.columns } #sözlük yapısı olarka her değişknedeki boş elema sayısı

df.isnull().sum() # her değişkendeki boş eleman sayısını veriyor !!!!
type(df.isnull().sum())
df.drop("who", axis=1, inplace=True).head()
################################## içi boş değişlkenlerin boşluklarını fillna ile doldurma
(df["deck"].mode())[0]
x = df["deck"].mode().astype("str", copy=True)
type(x)
df[df["deck"].isnull()]["deck"]
df.loc[df["deck"].isnull(), "deck"] = df.loc[df["deck"].isnull(), "deck"].fillna(value= df["deck"].mode()[0])  # burada nan olan boşlukları fillna kullanarak en çok tekrar eden(mod) deck olan C ile doldurduk
#not: df["deck"].mode() veri tipi bir pandas serisidir. serinin 0. index'i string bir ifadedir. dinamik olması açısından bu şekilde yapılmıştır
df.loc[df["deck"].isnull(), "deck"].fillna(value= df["deck"].mode()[0], inplace=True)  # burada nan olan boşlukları fillna kullanarak en çok tekrar eden(mod) deck olan C ile doldurduk
df["deck"].fillna(value=df["deck"].mode()[0], inplace=True)  #### en kısa ve güzel yol!!!
df["deck"].isnull().sum()
df["age"].median()
type(df["age"].median())
df["age"].isnull().sum()
df.loc[df["age"].isnull(), "age"] = df[df["age"].isnull()]["age"].fillna(value=df["age"].median())
df["age"].fillna(value=df["age"].median(), inplace=True)   #fillna kullanımı en kısa ve güzel yol !!!!
df.groupby(["pclass", "sex"]).agg({"survived" : ["mean", "median", "sum", "count"]})


df.groupby(["sex", "pclass"]).agg({"survived" : ["sum", "count", "mean"]})

def yas30(yas):
    if yas < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: yas30(x))
df["age_flag1"] = df["age"].apply(lambda x: 1 if x < 30 else 0)
df.head()

df = sns.load_dataset("tips")
df.head()
df.shape
df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})
df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})
df["day"].unique()

df2 = df[(df["sex"] == "Female") & (df["time"] == "Lunch" )]
df2.groupby("day")
df[(df["time"] == "Lunch" ) & (df["sex"] == "Female") ].groupby("day").agg({"total_bill": ["sum", "min", "max"],
                                                                           "tip" : ["sum", "min", "max"]})
df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].agg({"total_bill": ["count", "sum", "min", "max", "mean"]})
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()
df["total_bill_tip_sum"] = df[["total_bill", "tip"]].sum(axis=1)
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()
df2 = df["total_bill_tip_sum"].sort_values(ascending=False).head(30)
df3 = df.sort_values("total_bill_tip_sum", ascending=False)[:30]  #bu çok doğru olan değerdir !!!!
df3.shape

##############KURAL TABANLI SINIFLANDIRMA İLE POTANSİYLE MÜŞTERİ GETİRİSİ HESAPLAÖA

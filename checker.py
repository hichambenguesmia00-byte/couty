import time
import requests

def run_checker():
    while True:
        try:
            url = "https://algeria.blsspainglobal.com/DZA/Bls/DoorstepForm?data=..."
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            
            cookies = {

     "aws-waf-token": "d475c7fa-90da-45b4-8a16-96e24b255537:CQoAgfdcYd0uAgAA:doq402m/LgLuS5ER6UbHEeg8Fdox54NWbYDySLmnvVAcLZ4msYx36P3a4shqqqCXavWOEngnBRsGJNJRwEbFHJt1ZEMd2+9GaFLQTS7Bjk9lpNWgh9LH1pzqCyIEbKeFgoTdp7mDMo+8qgp7l+OTk9wemUK3utek9vMaWbYGsW+LsVHltV1CdmCHisr0VcugE/VpBw0akDmGMtQTicreQBKsaSTeil9sI4BSW+0fDnTYjZxVohpdWjIiinBaOWt5dCcNd65TtzwhODoOYHiBr6E=",
    ".AspNetCore.Cookies": "CfDJ8HR2AoMI3LpApkZfZPiNaiaU-HFDIMsJuBsJgV-x7qtIcv8QR_vpPguDEzSi1z8hR8zty_bMIfFQYcItCXcmnA5P4mn9I81DE5NMluYf7BRzRikhbeFmqIlx7VWlRQppCe2nq_jRC1dSYTi_0VW_Tlgk5wWqmvHIlzwhwjdhH3jNYqSenforoYIogrCN2zkHCbIA-STO8FotqqLQ5IapD6TYr47gBuszm-8be-FpF8KinN85dIm6iJsTPTyiswxSqwMrbTDRvHX3oto3U7YYvzE6dm0mMmPQNpNpWew4nXYDkAvDjXhqUtlYxjjs0DJkaymAnf5QZ7z-n6xD60TUCOAtiqYhU6Ef8JFn337_xH7QYh4JQtIysvX6Mv3GYf48nfIuDj-1ZVPAlVjChMTsZVEHfdlNBdlUcplTI8wPMJzKJMon5U04BA7swNCBQmQs8Zsp_EG6XayFe5ycuIo6yE7jkOrhZuphMko8pDXlgvyH4SwzPICFtoJLkgCRSWoxfu_SztzEstAOlWPmVGkdSAtFHL_8wka3zQ-4PCjGta5k_3GLHLEK18w3M3lDeyhgG5kF6CfNt0VtH5ULycb8Mbdlt9JfZp1yoaUuZj428rUbKEd2Dhmd5heZdofj2_IKUViaA4CnWyyeiPkfVEJga3oMwBcTDXH5ir0_z12b3oPKYZeR4sVmnLVIUgAyFkj4up7eyJhR0AdYARNIerc3RYarmKAC_VNFakJPz5yS9xgjX37ezIiqdhsLze37EyhoJhx993SnOMBSpqnQHeBtlVs4iIBJMJmSaPVzkpj0Co9bUqhKR_cGfZG9qNTxR6R2T0Y-JHYKLOj0BlqGlubPnT2Ig_pc9OtBx4GmrC48_5Ce4QovRlAZC2_mtL8Lq6-Mv7eCTkHpYtyIPE7gl5v5KvCIJXu2fKEmLVqEz-_AL9U2R882_5ThjHO2otXQvGFJNHb7Uq4Uca2FvODQPcwuA9ZFIhorHKwqsMQbjIQqH_ELIkNWfuGJJlEaWVFixG_LYaYXca4Q1RP1kQiK0aFBhlae06IxOa9k2RqfG458bsTUdafdU2oChBoC8nQjXD7ba7WLX7ClGJpMS9KQJCGjb6KmfsyXS4WqbN85Ahe96nTlvfyv9aW18aqcoP4uejK1183iLkehfVBgXQlGJhwA-aqMSV116ZuVWvz0-VKu8VECV_FVZlKuTbu3cONVQloOeYMPGBr6jCfo9onhj_v4T_ha_1TJkj5QJKjM9w8mPeXent4kixjzyuwOMnVX9R3YjoyukNFtYDStfTQAFPIqeChDszujlO19hSNrEaUjVVMWlmWlBa0F0WsQWBh1f-N_y1qsP0KTZeXHUt9YJgHUdU-WI4w_4B1RnYOuoT0Yi-scM0BN3SrQTRQhl3bVH5_QSVAxsxsyJG-1HeYmcS82oRnvrzEPQCaopd0oLvVnR84SRtzAHROtpnoULg5zXujEnmooTR0EFGVSq8ar-GlP-wb6GRZvpoU_XGQEMSfkuYWhWbk1kROFCt2u-qo8s547cLZydnlSsxi4zn_Ko7oeOKTOuqqeqir66M45waTrD5GPzMaZ7Gq_AsuhSGig1cJDr6X_Vceog_yGys9hhWmgNi030SO7f7ebeNaKjUO7LHQCuvn3-t9McsCJsdAMB8I-CeGSPSysmRvoCNKEPYxHcR-4DlOMSo0Bb6ROsW4FV4emDa_eyIdJno2Q7zDLNiF44VLGzEWXeCdDftBVjHLyjl4Qwv13ewhqsLUvpuNOAGVGFCM6Mr-eHbNaakA4jc-wgVEQnlroEHpEGDS1kAmr6XbIHnZl5rc1dW0TSiStcI4mjx3FeqpU8diU90CPe2Nn_DLI3NmCAYqZlFVHWCE-m866HGrdfWn2exl-rde_ifWrh9tJsJAgy6Dl3QbFNbKJrDQ_wE6vi2qcCZy_A0Ku_5AiNZ_asvIMSkx_vXsWbRbnSfWy76SqnnrHDlozBv46KgMF5F5Mab7I_a5UYEfXMUkkgAPi00zI1VDHOl11Ci0EMdDasN3H6bd5sW93VbS5VSFrk2CGJEO_6ajxz0YPBmd-KGv9A1PIUqe5uHfDPjjYT4Xg_X0o78Lk2-mxjqGn1KfVdOSjXov9jPxsBg_Rg_2mqPJnrroPnztT19gWfgdHaUL-9h6FtdzHCWMirnhz8mn-VskujX8j5LzL8DPcVnd-3PLrbW8c38jLI-SvPDIETu3sfdWnQcUwdgF-lK_bNAOQhxwpC--JWtjI0LXSLG_1H-o-8zfqf1LgT-I7-lJ-zEJeFRcWWAhHtFmyryDoHQIlw627Fdc4xL1BkmAn72GCTzPefsBvF9LN6h0dxuPL-QQ-vR1FeBan3GGuE4gcWzfxxQz_pjdJ_OEZidzSh7kwXVqGnPPGaRHb6K-i7IgMNJuIVV_pn4Qi-EfCrNrGxYktSKQ7jmBce7Zk-hpBm2uTaMRgf6fVwe5XnDpJt6NeDAEsY7mGWvMRfnC-6B2zJeYEPQ31Z0BPDOBtCgKU3Vc_iPozD1-RLJjiLURZlJSC1C9pTrGQLCULN4Y61vp0tCoo43ZIO_xQJe3OLKiXdvhgCvOHaJ_fdZIXaye51C0a-gyEb5shAB66X1jQlMKusfh3N2Ypq4fmnoweMe_XzjLkIcKGQfwX9ce42Gqsmc0CPYneR7S38m4civsJQGTcWhiCO-IhfU6tbsanw8xPQwaDu3RjEjO8iO_i6NEG8uTuqnWv-rY4PWZgJCM12McWRUPNoW03pJg-YJt1moRag9lhTjoEsetawMCNhQxTEUCCBfhq5GYMBtdnp-RfcQdbcZwTs3QPMvMt8cLPKxMfTL08cqoUsuXz2SPVaqzZIiMVkTNZELQyoGHhzpkrxrgr0BlAfkyPu331UCrnQeCVAxxvldyB-soms7PngVolOYYiwGgq9NTnEW6_QvC3Eyc4eBS6Z6JZZdm4c_TbaLjLKl8HGe3WsftCSDXw3_cCc3wXdkc3VWyN30oKsnMZDxN6FaLv5vk0VIMmNq8SqjTRakdHxPG_jxaWLVzx1t4tbRJs",
    ".AspNetCore.Antiforgery.xxx": "CfDJ8HR2AoMI3LpApkZfZPiNaiYkj2y24ik2dmUocCjoCkPoRW97wBP99i7jxtcbPzwouhXVQzauklzPDdMy6SbAO3YJw2NA1qDi_NLCl2gP6P-_V13i-I6CMeNQe9dlEURgH-mEq8_acj54wn2SDjr4BL4",  
    "visitorId_current": "3755893760"
            }
            
            r = requests.get(url, headers=headers, cookies=cookies, timeout=20)
            print("Status:", r.status_code)
            
            if "no slots are available" in r.text.lower():
                print("❌ لا توجد مواعيد حالياً")
            else:
                print("✅ قد تكون هناك مواعيد متاحة")
        
        except Exception as e:
            print("⚠️ Error:", e)
        
        time.sleep(120)  # يعاود المحاولة كل دقيقتين

# -*- coding: utf-8 -*-
#匯入firebase模組
from pyfirebase import Firebase
#指定firebase URL路徑
firebase = Firebase("https://changyee-1.firebaseio.com")
#指定資料層級
firebase_ref=firebase.ref("TW-CY/Time")
#Read Event Time
Event_Time=firebase_ref.get()
print Event_Time



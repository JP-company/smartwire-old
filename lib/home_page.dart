import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:sitwireapp/pushnotification_model.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_messaging/firebase_messaging.dart';

Future _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  print("백그라운드 메세지: ${message.messageId}");
}

class HomePage extends StatefulWidget {

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  PushNotification? _notificationInfo;
  String company = Get.arguments; // 코드를 받아옴
  late final FirebaseMessaging _messaging;

  void registerNotification() async{
    await Firebase.initializeApp();


    _messaging = FirebaseMessaging.instance;
    FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

    // ios 세팅
    NotificationSettings settings = await _messaging.requestPermission(
      alert: true,
      badge: true,
      provisional: false,
      sound: true,
    );

    if (settings.authorizationStatus == AuthorizationStatus.authorized){
      print("User granted the permission");

      //앱 켜져있을 때
      FirebaseMessaging.onMessage.listen((RemoteMessage message) {
        PushNotification notification = PushNotification.showNotification(
          title: message.notification!.title,
          body: message.notification!.body,
        ) as PushNotification;

        setState(() {
          _notificationInfo = notification;
        });
      });

      // 앱 백그라운드
      FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
        PushNotification notification = PushNotification.showNotification(
          title: message.notification!.title,
          body: message.notification!.body,
        ) as PushNotification;
        setState(() {
          _notificationInfo = notification;
        });
      });
    }
  }


  storeNotificationToken() async{
    String companyCode = '';
    if (company == 'wire_'){
      companyCode = 'sit';
    } else if (company == 'KM_wire_') {
      companyCode = 'km';
    }
    String? token = await FirebaseMessaging.instance.getToken();
    FirebaseFirestore.instance.collection('users').doc('company').collection(companyCode).doc(token).set(
        {
          'token': token
        },SetOptions(merge: true));
  }

  checkForInitialMessage() async{
    //앱 꺼져있을때
    RemoteMessage? initialMessage = await FirebaseMessaging.instance.getInitialMessage();
    if (initialMessage != null){
      PushNotification notification = PushNotification.showNotification(
        title: initialMessage.notification!.title,
        body: initialMessage.notification!.body,
      ) as PushNotification;
      setState(() {
        _notificationInfo = notification;
      });
    }
  }

  @override
  void initState() {
    // 일반
    registerNotification();
    // 앱 꺼져있을때
    checkForInitialMessage();
    // 토큰 저장
    storeNotificationToken();
    super.initState();

  }


  title() {
    if (company == 'wire_') {
      return 'SIT 와이어';
    } else if (company == 'KM_wire_'){
      return '광명와이어';
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text(title(),
          style: TextStyle(
            color: Colors.black,
            fontWeight: FontWeight.bold),), // #회사 이름#
        centerTitle: false,
        elevation: 0.5,
        backgroundColor: Colors.white,
        actions: [
          IconButton(
            icon: Icon(Icons.settings),
            onPressed: (){
              PushNotification.showNotification(
                title: '알림 설정 화면',
                body: '아직 준비중입니다.'
              );
            },
            color: Colors.black,
          )
        ],
      ),
      body: ListView(
        children: [Column(
              children: [
                Padding(
                    padding: EdgeInsets.fromLTRB(0, 25 , 0, 0),
                    child: WireCard(
                      company: company,
                      num: '1',
                    )
                ), // 1번 와이어

                Padding(
                  padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                  child: WireCard(
                    company: company,
                    num: '2',
                  )
                ), // 2번 와이어

                Padding(
                  padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                  child: WireCard(
                    company: company,
                    num: '3',
                  )
                ), // 3번 와이어

                Padding(
                  padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                  child: WireCard(
                    company: company,
                    num: '4',
                  ),
                ), // 4번 와이어
              ],
            ),
          ]
      ),
    );
  }
}


class WireCard extends StatelessWidget {

  const WireCard({Key? key, required this.company, required this.num}) : super(key: key);
  final company;
  final num;

  @override
  Widget build(BuildContext context) {
    if(company == 'wire_' && (num == '3' || num == '4')){
    return Container();
    } else {
      return StreamBuilder(
          stream: FirebaseFirestore.instance.collection(company + num).snapshots(),
          builder: (BuildContext context,
              AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(
                child: CircularProgressIndicator(),
              );
            } //렉 방지
            final docs_pre = snapshot.data!.docs;
            final last_date = docs_pre.length - 1;
            final date = docs_pre[last_date]['date'];
            return StreamBuilder(
                stream: FirebaseFirestore.instance.collection(company + num + '/dates/$date').snapshots(),
                builder: (BuildContext context,
                    AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot){
                  if(snapshot.connectionState == ConnectionState.waiting){
                    return Center(
                      child: CircularProgressIndicator(),
                    );
                  } //렉 방지
                  final docs = snapshot.data!.docs;
                  final last_sts = docs.length - 1;
                  final onoff = docs[last_sts]['onoff'];
                  final now = docs[last_sts]['now'];

                  dynamic wirename;
                  dynamic status;
                  dynamic shadowcolor;
                  dynamic bordersidecolor;
                  dynamic moving_image;
                  dynamic status_text_color;
                  dynamic status_time;


                  if(company == 'wire_'){
                    if(num == '1'){
                      wirename = '1번 와이어';
                    } else if(num == '2'){
                      wirename = '2번 와이어';
                    } else if(num == '3'){
                      wirename = '3번 와이어';
                    } else if(num == '4'){
                      wirename = '4번 와이어';
                    }
                  }
                  else if(company == 'KM_wire_'){
                    if(num == '1'){
                      wirename = '2호기';
                    } else if(num == '2'){
                      wirename = '3호기';
                    } else if(num == '3'){
                      wirename = '4호기';
                    } else if(num == '4'){
                      wirename = '5호기';
                    }
                  }

                  if(onoff == 'on'){
                    shadowcolor = Color(0xffD5FADC);
                    bordersidecolor = Color(0xff99FA95);
                    moving_image = 'assets/images/running.gif';
                    status_text_color = Color(0xff40B137);
                    status_time = '시작 시각: ';
                  } else if(onoff == 'finished'){
                    shadowcolor = Color(0xff2E64FE);
                    bordersidecolor = Color(0xff2E64FE);
                    moving_image = 'assets/images/done.png';
                    status_text_color = Color(0xff0040FF);
                    status_time = '완료 시각: ';
                  } else if(onoff == 'exit'){
                    shadowcolor = Color(0xffFFFF00);
                    bordersidecolor = Color(0xffFFFF00);
                    moving_image = 'assets/images/warning.png';
                    status_text_color = Color(0xffD7DF01);
                    status_time = '발생 시각: ';
                  } else {
                    shadowcolor = Color(0xffFFB1B1);
                    bordersidecolor = Color(0xffFFB1B1);
                    moving_image = 'assets/images/stop.png';
                    status_text_color = Color(0xffEB5B5B);
                    status_time = '정지 시각: ';
                  }

                  if(onoff == 'uncut'){
                    status = '와이어 선 씹힘';
                  } else if(onoff == 'nowire'){
                    status = '와이어 선 부족';
                  } else if(onoff == 'contact'){
                    status = '와이어 선 접촉';
                  } else if(onoff == 'moff'){
                    status = 'M코드 정지';
                  } else if(onoff == 'finished'){
                    status = '작업 완료';
                  } else if(onoff == 'pause'){
                    status = '와이어 미동작';
                  } else if(onoff == 'nowire'){
                    status = '와이어 선 부족';
                  } else if(onoff == 'off'){
                    status = '가동 정지';
                  } else if(onoff == 'on'){
                    status = '가동중';
                  } else if(onoff == 'exit'){
                    status = '알림 프로그램 꺼짐';
                  }

                  return ElevatedButton(
                      onPressed: (){
                        if(company == 'wire_'){
                          Future.delayed(Duration.zero, (){
                            if(num == '1'){
                              Get.toNamed("/home/date_page", arguments: 'wire_1');
                            } else if(num == '2'){
                              Get.toNamed("/home/date_page", arguments: 'wire_2');
                            }
                          });
                        }
                        else if(company == 'KM_wire_'){
                          Future.delayed(Duration.zero, () {
                            if(num == '1'){
                              Get.toNamed("/home/date_page", arguments: 'KM_wire_1');
                            } else if(num == '2'){
                              Get.toNamed("/home/date_page", arguments: 'KM_wire_2');
                            } else if(num == '3'){
                              Get.toNamed("/home/date_page", arguments: 'KM_wire_3');
                            } else if(num == '4'){
                              Get.toNamed("/home/date_page", arguments: 'KM_wire_4');
                            }
                          });
                        }
                      },
                      style: OutlinedButton.styleFrom(
                          minimumSize: Size(
                              MediaQuery.of(context).size.width * 0.9,
                              100.0
                          ),
                          backgroundColor: Colors.white,
                          shadowColor: shadowcolor,
                          elevation: 3,
                          side: BorderSide(
                              color: bordersidecolor,
                              width: 1.0
                          ),
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(22.0)
                          )
                      ),
                      child: Row(
                          mainAxisSize: MainAxisSize.min,
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [Column(
                            children: [
                              Container(
                                child: Text(wirename, style: TextStyle(
                                    fontSize: 15.0,
                                    color: Color(0xff4E4E4E)
                                ),
                                ),
                                width: MediaQuery.of(context).size.width * 0.6,
                              ), // 1번 와이어
                              Padding(
                                padding: EdgeInsets.fromLTRB(0, 6, 0, 6),
                                child: Container(
                                  child: Text(status,
                                    style: TextStyle(
                                        color:status_text_color,
                                        fontSize: 16.0,
                                        fontWeight: FontWeight.bold
                                    ),
                                  ),
                                  width: MediaQuery.of(context).size.width * 0.6,
                                ),
                              ), // 가동중
                              Container(
                                child: Text(status_time + '$date $now',
                                  style:
                                  TextStyle(
                                      color:Color(0xff9E9E9E),
                                      fontSize: 14.0
                                  ),
                                ),
                                width: MediaQuery.of(context).size.width * 0.6,
                              ), // 시작 시각
                            ],
                          ),
                            Container(
                              child: Image.asset(moving_image),
                              width: 64.0,
                            ),
                          ]
                      )
                  ); // 가동중
                }
            );
          }
      );
    }
  }
}

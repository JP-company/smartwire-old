import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:overlay_support/overlay_support.dart';
import 'package:sitwireapp/alarm_setting.dart';
import 'package:sitwireapp/functions/main_card.dart';
import 'package:sitwireapp/services/local_notification_service.dart';
import 'package:sitwireapp/wire1_page.dart';
import 'package:sitwireapp/wire2_page.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'main.dart';

Future _firebaseMessagingBackgroundHandler(RemoteMessage message) async{
  print("Handling a background message: ${message.messageId}");
}


class HomePage extends StatefulWidget {

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  String company = Get.arguments; // 코드를 받아옴


  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          title: Text('SIT와이어', style: TextStyle(
              color: Colors.black,
              fontWeight: FontWeight.bold),), // #회사 이름#
          centerTitle: false,
          elevation: 0.5,
          backgroundColor: Colors.white,
          actions: [
            IconButton(
              icon: Icon(Icons.settings),
              onPressed: (){
                Get.to(AlarmSetting());
              },
              color: Colors.black,
            )
          ],
        ),
        body: ListView(
          children: [Column(
              children: [
                  Padding(
                    padding: EdgeInsets.fromLTRB(0, 30, 0, 0),
                    child: StreamBuilder(
                        stream: FirebaseFirestore.instance.collection('$company' +'1').snapshots(), // wire_1 문서
                        builder: (BuildContext context,
                            AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
                          if (snapshot.connectionState == ConnectionState.waiting) {
                            return Center(
                              child: CircularProgressIndicator(),
                            );
                          } //렉 방지
                          final docs_pre = snapshot.data!.docs; // wire_1의 문서를 모두 불러옴
                          final last_date = docs_pre.length - 1; // wire_1 문서길이에 1을 뺌(마지막 문서 확인)
                          final date = docs_pre[last_date]['date']; // 마지막 문서의 'date' 값
                          return StreamBuilder(
                              stream: FirebaseFirestore.instance.collection('$company' + '1/dates/$date').snapshots(), // wire_1/date/date 문서
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
                                if(onoff == 'on'){
                                  return ElevatedButton(
                                      onPressed: (){Get.to(Wire1Page());},
                                      style: OutlinedButton.styleFrom(
                                          minimumSize: Size(
                                              300.0,
                                              300.0
                                          ),
                                          backgroundColor: Colors.white,
                                          shadowColor: Color(0xffD5FADC),
                                          elevation: 3,
                                          side: BorderSide(
                                              color: Color(0xff99FA95),
                                              width: 1.0
                                          )
                                      ),
                                      child: Column(children: [
                                        Padding(
                                          padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                                          child: Text('1번 와이어', style: TextStyle(
                                              fontSize: 15.0,
                                              color: Color(0xff4E4E4E)
                                          ),),
                                        ), // 1번 와이어
                                        Image.asset('assets/images/working.gif'), // 움짤
                                        Padding(
                                          padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
                                          child: Text('가동중...',
                                            style: TextStyle(
                                                color:Color(0xff40B137),
                                                fontSize: 16.0,
                                                fontWeight: FontWeight.bold
                                            ),
                                          ),
                                        ), // 가동중
                                        Padding(
                                            padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                                            child: Text('시작 시각: $date $now',
                                              style:
                                              TextStyle(
                                                  color:Color(0xff9E9E9E),
                                                  fontSize: 16.0
                                              ),
                                            )
                                        ) // 시작 시각
                                      ],
                                      )
                                  ); // 가동중 버튼
                                }
                                else{
                                  return ElevatedButton(
                                      onPressed: (){Get.to(Wire1Page());},
                                      style: OutlinedButton.styleFrom(
                                          minimumSize: Size(
                                              300.0,
                                              300.0
                                          ),
                                          backgroundColor: Colors.white,
                                          shadowColor: Color(0xffFFB1B1),
                                          elevation: 3,
                                          side: BorderSide(
                                              color: Color(0xffFFB1B1),
                                              width: 1.0
                                          )
                                      ),
                                      child: Column(children: [
                                        Padding(
                                          padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                                          child: Text('1번 와이어', style: TextStyle(
                                              fontSize: 15.0,
                                              color: Color(0xff4E4E4E)
                                          ),),
                                        ), // 1번 와이어
                                        Image.asset('assets/images/working_stop.jpg'), // 움짤
                                        Padding(
                                          padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
                                          child: Text('가동 정지',
                                            style: TextStyle(
                                                color:Color(0xffEB5B5B),
                                                fontSize: 16.0,
                                                fontWeight: FontWeight.bold
                                            ),
                                          ),
                                        ), // 가동 정지
                                        Padding(
                                          padding: EdgeInsets.fromLTRB(0, 5, 0, 0),
                                          child: Text('M코드 정지',
                                            style: TextStyle(
                                                color:Color(0xff4E4E4E),
                                                fontSize: 12.0,
                                                fontWeight: FontWeight.bold
                                            ),
                                          ),
                                        ), // 가동 정지
                                        Padding(
                                            padding: EdgeInsets.fromLTRB(0, 10, 0, 0),
                                            child: Text('정지 시각: $date $now',
                                              style:
                                              TextStyle(
                                                  color:Color(0xff9E9E9E),
                                                  fontSize: 16.0
                                              ),
                                            )
                                        ), // 정지 시각
                                      ],
                                      )
                                  ); // 가동정지 버튼
                                }
                              }
                          );
                        }
                    )
                    ), // 1번 와이어
                  Padding(
                  padding: EdgeInsets.fromLTRB(0, 30, 0, 0),
                  child: StreamBuilder(
                      stream: FirebaseFirestore.instance.collection('$company' + '2').snapshots(),
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
                            stream: FirebaseFirestore.instance.collection('$company' + '2/dates/$date').snapshots(),
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
                              if(onoff == 'on'){
                                return ElevatedButton(
                                    onPressed: (){Get.to(Wire2Page());},
                                    style: OutlinedButton.styleFrom(
                                        minimumSize: Size(
                                            300.0,
                                            300.0
                                        ),
                                        backgroundColor: Colors.white,
                                        shadowColor: Color(0xffD5FADC),
                                        elevation: 3,
                                        side: BorderSide(
                                            color: Color(0xff99FA95),
                                            width: 1.0
                                        )
                                    ),
                                    child: Column(children: [
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                                        child: Text('2번 와이어', style: TextStyle(
                                            fontSize: 15.0,
                                            color: Color(0xff4E4E4E)
                                        ),),
                                      ), // 2번 와이어
                                      Image.asset('assets/images/working.gif'), // 움짤
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
                                        child: Text('가동중...',
                                          style: TextStyle(
                                              color:Color(0xff40B137),
                                              fontSize: 16.0,
                                              fontWeight: FontWeight.bold
                                          ),
                                        ),
                                      ), // 가동중
                                      Padding(
                                          padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                                          child: Text('시작 시각: $date $now',
                                            style:
                                            TextStyle(
                                                color:Color(0xff9E9E9E),
                                                fontSize: 16.0
                                            ),
                                          )
                                      ) // 시작 시각
                                    ],
                                    )
                                ); // 가동중 버튼
                              }else{
                                return ElevatedButton(
                                    onPressed: (){Get.to(Wire2Page());},
                                    style: OutlinedButton.styleFrom(
                                        minimumSize: Size(
                                            300.0,
                                            300.0
                                        ),
                                        backgroundColor: Colors.white,
                                        shadowColor: Color(0xffFFB1B1),
                                        elevation: 3,
                                        side: BorderSide(
                                            color: Color(0xffFFB1B1),
                                            width: 1.0
                                        )
                                    ),
                                    child: Column(children: [
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                                        child: Text('2번 와이어', style: TextStyle(
                                            fontSize: 15.0,
                                            color: Color(0xff4E4E4E)
                                        ),),
                                      ), // 2번 와이어
                                      Image.asset('assets/images/working_stop.jpg'), // 움짤
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
                                        child: Text('가동 정지',
                                          style: TextStyle(
                                              color:Color(0xffEB5B5B),
                                              fontSize: 16.0,
                                              fontWeight: FontWeight.bold
                                          ),
                                        ),
                                      ), // 가동 정지
                                      Padding(
                                          padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                                          child: Text('정지 시각: $date $now',
                                            style:
                                            TextStyle(
                                                color:Color(0xff9E9E9E),
                                                fontSize: 16.0
                                            ),
                                          )
                                      ), // 정지 시각
                                    ],
                                    )
                                ); // 가동정지 버튼
                              }
                            }
                        );
                      }
                  ),
                ), // 2번 와이어
                ],
              ),
          ]
        ),

    );
  }
}

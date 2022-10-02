import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class Wire2Page extends StatelessWidget {

  String company = Get.arguments; // 코드를 받아옴

  @override
  Widget build(BuildContext context) {


    return Scaffold(
      appBar: AppBar(
        title: Text('2번 와이어 가동 기록',style: TextStyle(
            color: Colors.black
        ),),
        leading: IconButton(
          onPressed: (){
            Navigator.pop(context);
          },
          color: Colors.black,
          icon: Icon(Icons.arrow_back_ios),
        ),
        centerTitle: false,
        elevation: 0.5,
        backgroundColor: Colors.white,
      ),
      body:
      StreamBuilder(
        stream: FirebaseFirestore.instance.collection('$company' + '2').snapshots(),
        builder: (BuildContext context,
            AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: CircularProgressIndicator(),
            );
          }
          final docs = snapshot.data!.docs;
          return ListView.builder(
                itemCount: docs.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    onTap: () {
                      if ('$company' == 'wire_'){
                        Get.toNamed("/home/wire1page/detail_page2", arguments: docs[(docs.length - 1) - index]['date']); //wire_1 문서(docs)에 'index'번쨰의 date 값
                      } else if('$company' == 'KM_wire_'){
                        Get.toNamed("/home/wire1page/detail_page2_km", arguments: docs[(docs.length - 1) - index]['date']); //wire_1 문서(docs)에 'index'번쨰의 date 값
                      }
                    },
                    title: Text(docs[(docs.length - 1) - index]['date'],
                      style: TextStyle(
                          fontSize: 20.0
                      ),
                    ),
                  );
                }
          );
        },
      ),


    );
  }


}

// Padding(
//               padding: EdgeInsets.fromLTRB(0, 30, 0, 0),
//               child: StreamBuilder(
//                   stream: FirebaseFirestore.instance.collection('wire_1/dates/2022-01-28').snapshots(),
//                   builder: (BuildContext context,
//                       AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot){
//                     if(snapshot.connectionState == ConnectionState.waiting){
//                       return Center(
//                         child: CircularProgressIndicator(),
//                       );
//                     } //렉 방지
//                     final docs = snapshot.data!.docs;
//                     final last_sts = docs.length - 1;
//                     final onoff = docs[last_sts]['onoff'];
//                     if(onoff == 'on'){
//                       return ElevatedButton(
//                           onPressed: (){Get.to(Wire1Page());},
//                           style: OutlinedButton.styleFrom(
//                               minimumSize: Size(
//                                   300.0,
//                                   300.0
//                               ),
//                               backgroundColor: Colors.white,
//                               shadowColor: Color(0xffD5FADC),
//                               elevation: 3,
//                               side: BorderSide(
//                                   color: Color(0xff99FA95),
//                                   width: 1.0
//                               )
//                           ),
//                           child: Column(children: [
//                             Padding(
//                               padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
//                               child: Text('1번 와이어', style: TextStyle(
//                                   fontSize: 15.0,
//                                   color: Color(0xff4E4E4E)
//                               ),),
//                             ), // 1번 와이어
//                             Image.asset('assets/images/working.gif'), // 움짤
//                             Padding(
//                               padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
//                               child: Text('가동중...',
//                                 style: TextStyle(
//                                     color:Color(0xff40B137),
//                                     fontSize: 16.0,
//                                     fontWeight: FontWeight.bold
//                                 ),
//                               ),
//                             ), // 가동중
//                             Padding(
//                                 padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
//                                 child: Text('시작 시각: 2022-01-31 19:30:30',
//                                   style:
//                                   TextStyle(
//                                       color:Color(0xff9E9E9E),
//                                       fontSize: 16.0
//                                   ),
//                                 )
//                             ) // 시작 시각
//                           ],
//                           )
//                       ); // 가동 중 버튼
//                     }else{
//                       return ElevatedButton(
//                           onPressed: (){Get.to(Wire1Page());},
//                           style: OutlinedButton.styleFrom(
//                               minimumSize: Size(
//                                   300.0,
//                                   300.0
//                               ),
//                               backgroundColor: Colors.white,
//                               shadowColor: Color(0xffFFB1B1),
//                               elevation: 3,
//                               side: BorderSide(
//                                   color: Color(0xffFFB1B1),
//                                   width: 1.0
//                               )
//                           ),
//                           child: Column(children: [
//                             Padding(
//                               padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
//                               child: Text('1번 와이어', style: TextStyle(
//                                   fontSize: 15.0,
//                                   color: Color(0xff4E4E4E)
//                               ),),
//                             ), // 1번 와이어
//                             Image.asset('assets/images/working_stop.tiff'), // 움짤
//                             Padding(
//                               padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
//                               child: Text('가동 정지',
//                                 style: TextStyle(
//                                     color:Color(0xffEB5B5B),
//                                     fontSize: 16.0,
//                                     fontWeight: FontWeight.bold
//                                 ),
//                               ),
//                             ), // 가동 정지
//                             Padding(
//                                 padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
//                                 child: Text('정지 시각: 2022-01-31 19:30:30',
//                                   style:
//                                   TextStyle(
//                                       color:Color(0xff9E9E9E),
//                                       fontSize: 16.0
//                                   ),
//                                 )
//                             ), // 정지 시각
//                           ],
//                           )
//                       ); // 가동 정지 버튼
//                     }
//                   }
//               ),
//             )
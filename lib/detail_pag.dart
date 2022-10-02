import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';



class DetailPage1 extends StatelessWidget {


  @override
  Widget build(BuildContext context) {

    String date = Get.arguments; // docs[index]['date'] 값을 받아옴

    return Scaffold(
      appBar: AppBar(
        title: Text('1번 $date',style: TextStyle(
            color: Colors.black),),
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
      body: StreamBuilder(
        stream: FirebaseFirestore.instance.collection('wire_1/dates/$date').snapshots(),
        builder: (BuildContext context,
            AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
          if(snapshot.connectionState == ConnectionState.waiting){
            return Center(
              child: CircularProgressIndicator(),
            );
          } //렉 방지
          final docs = snapshot.data!.docs;
          return ListView.builder(
              itemCount: docs.length,
              itemBuilder: (context, index){
                final onoff = docs[index]['onoff'];

                dynamic onofftext;
                dynamic onoffcolor;
                dynamic onoffstatus;

                if(onoff == 'on'){
                  onofftext = 'ON';
                  onoffcolor = Colors.green;
                  onoffstatus = '';
                } else if (onoff == 'off') {
                  onofftext = 'OFF';
                  onoffcolor = Colors.red;
                  onoffstatus = '';
                } else if (onoff == 'uncut') {
                  onofftext = 'OFF';
                  onoffcolor = Colors.red;
                  onoffstatus = '   와이어 선 씹힘';
                } else if (onoff == 'nowire') {
                  onofftext = 'OFF';
                  onoffcolor = Colors.red;
                  onoffstatus = '   와이어 선 부족';
                } else if (onoff == 'contact') {
                  onofftext = 'OFF';
                  onoffcolor = Colors.red;
                  onoffstatus = '   와이어 선 접촉';
                } else if (onoff == 'pause') {
                  onofftext = 'OFF';
                  onoffcolor = Colors.red;
                  onoffstatus = '   와이어 미동작';
                } else if (onoff == 'moff') {
                  onofftext = 'OFF';
                  onoffcolor = Colors.red;
                  onoffstatus = '   M코드 정지';
                } else if (onoff == 'finished') {
                  onofftext = 'FIN';
                  onoffcolor = Colors.blue;
                  onoffstatus = '   작업 완료';
                } else if (onoff == 'exit') {
                  onofftext = 'ERR';
                  onoffcolor = Color(0xffD7DF01);
                  onoffstatus = '   알림 프로그램 애러';
                }

                return ListTile(
                  title: Text(docs[index]['now'] + onoffstatus,
                    style: TextStyle(
                      fontSize:  18.0,
                    ),),
                  leading:
                  Text(onofftext,
                      style:TextStyle(
                          fontSize: 18.0,
                          color: onoffcolor,
                          fontWeight: FontWeight.bold
                      )),
                );

              }
          );
        } ,
      ),);

  }
}

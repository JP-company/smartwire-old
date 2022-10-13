import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class DatePage extends StatelessWidget {


  String company = Get.arguments; // 코드를 받아옴
  dynamic title;


  @override
  Widget build(BuildContext context) {
    if(company == "wire_1"){
      title = '1번 와이어 가동 기록';
    } else if(company == "wire_2"){
      title = '2번 와이어 가동 기록';
    } else if(company == "KM_wire_1"){
      title = '2호기 가동 기록';
    } else if(company == "KM_wire_2"){
      title = '3호기 가동 기록';
    } else if(company == "KM_wire_3"){
      title = '4호기 가동 기록';
    } else if(company == "KM_wire_4"){
      title = '5호기 가동 기록';
    }
    return Scaffold(
      appBar: AppBar(
        title: Text(title,style: TextStyle(
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
        stream: FirebaseFirestore.instance.collection(company).snapshots(),
        builder: (BuildContext context,
            AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: CircularProgressIndicator(),
            );}

          final docs = snapshot.data!.docs;
          return ListView.builder(
              itemCount: docs.length,
              itemBuilder: (context, index) {
                return ListTile(
                  onTap: () {
                    Future.delayed(Duration.zero, () {
                      Get.toNamed("/home/date_page/time_page",
                          arguments: {'date' : docs[(docs.length - 1) - index]['date'], 'wire' : company}
                      );
                    });//wire_1 문서(docs)에 'index'번쨰의 date 값
                  },
                  title: Text(
                    docs[(docs.length - 1) - index]['date'],
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

class Arguments {
  final String date;
  final String wire;

  Arguments(this.date, this.wire);
}
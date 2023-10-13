import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class DatePage extends StatelessWidget {


  String company = Get.arguments; // 코드를 받아옴
  dynamic title;
  dynamic path;

  @override
  Widget build(BuildContext context) {
    if(company == "sit1"){
      title = '1호기 가동 기록'; path = "sit";
    } else if(company == "sit2"){
      title = '2호기 가동 기록'; path = "sit";
    } else if(company == "km2"){
      title = '2호기 가동 기록'; path = "km";
    } else if(company == "km3"){
      title = '3호기 가동 기록'; path = "km";
    } else if(company == "km5"){
      title = '5호기 가동 기록'; path = "km";
    } else if(company == "km6"){
      title = '6호기 가동 기록'; path = "km";
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
        stream: FirebaseFirestore.instance.collection("company/" + path + "/" + company).snapshots(),
        builder: (BuildContext context,
            AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: CircularProgressIndicator(),
            );}

          final docs = snapshot.data!.docs;
          dynamic dateArr = docs[docs.length -1]['date'].split(" ");


          return ListView.builder(
              itemCount: dateArr.length,
              itemBuilder: (context, index) {
                return ListTile(
                  onTap: () {
                    Future.delayed(Duration.zero, () {
                      Get.toNamed("/home/date_page/time_page",
                          arguments: {'date' : dateArr[(dateArr.length - 1) - index], 'wire' : company}
                      );
                    });//wire_1 문서(docs)에 'index'번쨰의 date 값
                  },
                  title: Text(
                    dateArr[(dateArr.length - 1) - index],
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

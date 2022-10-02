import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class Wire1Page extends StatelessWidget {


  String company = Get.arguments; // 코드를 받아옴

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('1번 와이어 가동 기록',style: TextStyle(
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
        stream: FirebaseFirestore.instance.collection('$company' + '1').snapshots(),
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
                    if ('$company' == 'wire_'){
                      Get.toNamed("/home/wire1page/detail_page1", arguments: docs[(docs.length - 1) - index]['date']); //wire_1 문서(docs)에 'index'번쨰의 date 값
                    } else if('$company' == 'KM_wire_'){
                      Get.toNamed("/home/wire1page/detail_page1_km", arguments: docs[(docs.length - 1) - index]['date']); //wire_1 문서(docs)에 'index'번쨰의 date 값
                    }
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
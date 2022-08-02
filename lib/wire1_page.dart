import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:last/detail_pag.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class Wire1Page extends StatelessWidget {


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
        stream: FirebaseFirestore.instance.collection('wire_1').snapshots(),
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
                    Get.to(DetailPage1(index), arguments: docs[index]['date']);
                  },
                  title: Text(
                      docs[index]['date'],
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

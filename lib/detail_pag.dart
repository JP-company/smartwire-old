import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class DetailPage1 extends StatelessWidget {

  final int id;

  const DetailPage1(this.id);

  @override
  Widget build(BuildContext context) {

    String date = Get.arguments;

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
                if(onoff == 'on'){
                  return ListTile(
                    title: Text(docs[index]['now'],
                      style: TextStyle(
                        fontSize:  18.0,
                      ),),
                    leading:
                    Text('ON',
                        style:TextStyle(
                          fontSize: 18.0,
                          color: Colors.green,
                          fontWeight: FontWeight.bold
                        )),
                  );
                } else{
                  return ListTile(
                    title: Text(docs[index]['now'],
                      style: TextStyle(
                        fontSize:  18.0,
                      ),),
                    leading:
                    Text('OFF',
                        style:TextStyle(
                            fontSize: 18.0,
                            color: Colors.red,
                            fontWeight: FontWeight.bold
                        )),
                  );

                }

              }
          );
        } ,
      ),);

  }
}

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:get/get_core/src/get_main.dart';
import 'package:get/get_navigation/get_navigation.dart';



class TimePage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {

    String date = Get.arguments['date'];
    String wire = Get.arguments['wire'];
    dynamic title;
    dynamic path;

    if(wire == "sit1"){
      title = '1호기'; path = "sit";
    } else if(wire == "sit2"){
      title = '2호기'; path = "sit";
    } else if(wire == "km2"){
      title = '2호기'; path = "km";
    } else if(wire == "km3"){
      title = '3호기'; path = "km";
    } else if(wire == "km5"){
      title = '5호기'; path = "km";
    } else if(wire == "km6"){
      title = '6호기'; path = "km";
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(title + ' ' + date,style: TextStyle(
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
        stream: FirebaseFirestore.instance.collection("company/" + path + "/" + wire + '/Logs/$date').snapshots(),
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
                final onoff = docs[(docs.length - 1) - index]['log'];

                dynamic onofftext;
                dynamic onoffcolor;
                dynamic onoffstatus;

                if(onoff == 'start' || onoff == 'start_restart' || onoff == 'on' || onoff == 'start_restart_detected' || onoff == 'start_autostart'){
                  onofftext = 'ON';
                  onoffcolor = Colors.green;
                } else if (onoff == 'stop_finished' || onoff == 'finished') {
                  onofftext = 'FIN';
                  onoffcolor = Colors.blue;
                } else if (onoff == 'exit') {
                  onofftext = 'ERR';
                  onoffcolor = Color(0xffD7DF01);
                } else {
                  onofftext = 'OFF';
                  onoffcolor = Colors.red;
                }

                if(onoff == 'stop' || onoff == 'off'){
                  onoffstatus = '   가공 정지';
                } else if(onoff == 'start_restart'){
                  onoffstatus = '   가공 재시작';
                } else if(onoff == 'start_restart_detected'){
                  onoffstatus = '   [가공 감지]가공 재시작';
                } else if(onoff == 'start_autostart'){
                  onoffstatus = '   [프로그램]오토스타트';
                } else if(onoff == 'start'){
                  onoffstatus = '   작업 시작';
                } else if(onoff == 'stop_moff'){
                  onoffstatus = '   M코드 정지';
                } else if(onoff == 'stop_contact'){
                  onoffstatus = '   와이어 접촉';
                } else if(onoff == 'stop_contact_30s'){
                  onoffstatus = '   와이어 30초 접촉';
                } else if(onoff == 'stop_cut'){
                  onoffstatus = '   작업중 와이어 단선';
                } else if(onoff == 'stop_reset'){
                  onoffstatus = '   Reset';
                } else if(onoff == 'stop_wire_notworking'){
                  onoffstatus = '   와이어 미동작';
                } else if(onoff == 'stop_liquid_notworking'){
                  onoffstatus = '   가공액 미동작';
                } else if(onoff == 'stop_insert_failure'){
                  onoffstatus = '   자동결선 삽입실패(M20)';
                } else if(onoff == 'stop_cut_failure'){
                  onoffstatus = '   자동결선 절단실패(M21)';
                } else if(onoff == 'stop_cleanup_failure'){
                  onoffstatus = '   자동결선 잔여와이어 처리실패(M21)';
                } else if(onoff == 'stop_feed_motor_alarm'){
                  onoffstatus = '   자동결선 Feed Motor Alarm!!';
                } else if(onoff == 'stop_auto_cut_failure'){
                  onoffstatus = '   자동결선 절단 공정 실패';
                } else if(onoff == 'stop_auto_cleanup_failure'){
                  onoffstatus = '   자동결선 잔여와이어 처리실패';
                } else if(onoff == 'stop_lowerpart_contact'){
                  onoffstatus = '   자동결선 하부 뭉치 Wire Contact!!';
                } else if(onoff == 'stop_upperpart_contact'){
                  onoffstatus = '   자동결선 상부 센서 Wire Contact!!';
                } else if(onoff == 'stop_awf_sensor'){
                  onoffstatus = '   AWF 명령끝날때까지 센서감지 안됨';
                } else if(onoff == 'stop_single_block_stop'){
                  onoffstatus = '   작업중 Single Block Stop';
                } else if(onoff == 'stop_bobbin_wirecut'){
                  onoffstatus = '   보빈 와이어 단선';
                } else if(onoff == 'stop_fluid_sensor'){
                  onoffstatus = '   오일센서 이상 감지';
                } else if(onoff == 'stop_door_sensor'){
                  onoffstatus = '   자동문센서 이상 감지';
                } else if(onoff == 'ready_on'){
                  onoffstatus = '   Ready On';
                } else if(onoff == 'ready_off'){
                  onoffstatus = '   Ready Off';
                } else if(onoff == 'stop_emergency'){
                  onoffstatus = '   비상정지';
                } else if(onoff == 'stop_collect_breakaway'){
                  onoffstatus = '   회수부 와이어 이탈';
                } else if(onoff == 'stop_finished' || onoff == 'finished'){
                  onoffstatus = '   작업 완료';
                } else if(onoff == 'stop_initialization'){
                  onoffstatus = '   와이어 기계 연결 완료';
                } else if(onoff == 'stop_closed'){
                  onoffstatus = '   와이어 기계 전원 종료됨';
                } else if(onoff == 'stop_disconnected'){
                  onoffstatus = '   와이어 기계 연결 끊어짐';
                } else if(onoff == 'stop_open_succeeded'){
                  onoffstatus = '   와이어 기계 전원 켜짐';
                } else if(onoff == 'exit'){
                  onoffstatus = '   알림 프로그램 오류';
                } else if(onoff == 'on'){
                  onoffstatus = '   작업 시작';
                } else {
                  onoffstatus = '';
                }


                return ListTile(
                  title: Text(docs[(docs.length - 1) - index]['time'] + onoffstatus,
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

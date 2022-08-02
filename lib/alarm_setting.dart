import 'package:flutter/material.dart';

class AlarmSetting extends StatefulWidget {
  const AlarmSetting({Key? key}) : super(key: key);

  @override
  _AlarmSettingState createState() => _AlarmSettingState();
}

class _AlarmSettingState extends State<AlarmSetting> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          title: Text('알림 설정',style: TextStyle(
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

    );
  }
}

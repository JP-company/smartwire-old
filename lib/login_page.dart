import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:last/alarm_setting.dart';
import 'package:last/functions/main_card.dart';
import 'package:last/pushnotification_model.dart';
import 'package:last/services/local_notification_service.dart';
import 'package:last/wire1_page.dart';
import 'package:last/wire2_page.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_messaging/firebase_messaging.dart';


class LoginPage extends StatelessWidget {
  const LoginPage({Key? key}) : super(key: key);

  Widget _userIdWidget(){
    return TextFormField(
      keyboardType: TextInputType.emailAddress,
      decoration: const InputDecoration(
        border: OutlineInputBorder(),
        labelText: '코드를 입력해주세요',
      ),
      validator: (String? value){
        if (value!.isEmpty) {// == null or isEmpty
          return '코드를 입력해주세요.';
        }
        return null;
      },
    );
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Center(
            child: _userIdWidget()),
      ),
    );
  }
}

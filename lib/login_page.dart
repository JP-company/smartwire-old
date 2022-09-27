<<<<<<< HEAD

=======
import 'package:firebase_core/firebase_core.dart';
>>>>>>> parent of 2c51c96 (220927)
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:sitwireapp/alarm_setting.dart';
import 'package:sitwireapp/database/db.dart';
import 'package:sitwireapp/database/memo.dart';
import 'package:sitwireapp/detail_pag.dart';
import 'package:sitwireapp/functions/main_card.dart';
import 'package:sitwireapp/home_page.dart';
import 'package:sitwireapp/pushnotification_model.dart';
import 'package:sitwireapp/services/local_notification_service.dart';
import 'package:sitwireapp/wire1_page.dart';
import 'package:sitwireapp/wire2_page.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_messaging/firebase_messaging.dart';


class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  TextEditingController controller = TextEditingController(); //입력되는 값을 제어
  String code = '';

  Widget _CodeInputWidget() {
    return Container(
      padding: EdgeInsets.fromLTRB(20, 0, 20, 10),
      child: TextField(
        controller: controller,
        keyboardType: TextInputType.emailAddress,
        decoration: const InputDecoration(
          border: OutlineInputBorder(),
          labelText: '코드를 입력해주세요.',
        ),
      ),
    );
  }



  Widget _ButtonWidget() {
    return Container(
      padding: EdgeInsets.fromLTRB(60, 0, 60, 0),
      child: ElevatedButton(
          child: Container(
            height: 40,
            width: double.infinity,
            alignment: Alignment.center,
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(1),
                color: Colors.blue
            ),
            child: Text("실행하기",
              style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 20
              ),
              textAlign: TextAlign.center,
            ),
          ),
          onPressed: () {
            if (controller.text == 'sit') {
              Get.offNamed("/home", arguments: 'wire_');
            } else if (controller.text == 'gm') {
              Get.offNamed("/home", arguments: 'KM_wire_');
            }
            // 여기서 코드에 따라 다른 값을 넘겨주면 됨
          }

      ),
    );
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
<<<<<<< HEAD
      body: Center(
        child: FutureBuilder<List<Code>>(
          future: DatabaseHelper.instance.getCodes(),
          builder: (BuildContext context, AsyncSnapshot<List<Code>>snapshot) {
            return Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    width: 1,
                    height: 1,
                    child: ListView(
                      children: snapshot.data!.map((code) {
                        if(code.name == 'sit'){
                          Get.toNamed("/home", arguments: 'wire_');
                        } else if (code.name == 'gm'){
                          Get.toNamed("/home", arguments: 'KM_wire_');
                        }
                        return Center(
                          child: Text(code.name),
                        );
                      }).toList(),
                    ),
                  ),
                  _CodeInputWidget(),
                  _ButtonWidget(),
                ]
            );
          },
        ),
      ),
=======
        body: Form(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              _CodeInputWidget(),
              _ButtonWidget()
            ],
          ),)
>>>>>>> parent of 2c51c96 (220927)
    );
  }


  Future <void> saveDB() async {
    DBHelper sd = DBHelper();
    var fido = Memo(
        id: 3,
        code: 'sit0871'
    );
    await sd.insertMemo(fido);
    print(await sd.memos());
  }
<<<<<<< HEAD


  Future _onCreate(Database db, int version) async {
    await db.execute('''
      CREATE TABLE codes(
        id INTEGER PRIMARY KEY,
        name TEXT
      )
      ''');
  }


  Future<List<Code>> getCodes() async {
    Database db = await instance.database;
    var codes = await db.query('codes', orderBy: 'name');
    List<Code> codeList = codes.isNotEmpty
        ? codes.map((c) => Code.fromMap(c)).toList()
        : [];
    return codeList;
  }

  Future<int> add(Code code) async {
    Database db = await instance.database;
    return await db.insert('codes', code.toMap());
  }

  Future<int> remove(int id) async {
    Database db = await instance.database;
    return await db.delete('codes', where: 'id = ?', whereArgs:  [id]);
  }

=======
>>>>>>> parent of 2c51c96 (220927)
}
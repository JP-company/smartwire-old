import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:sqflite/sqflite.dart';
import 'dart:io';
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';


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
  } // 텍스트필드

  Widget _ButtonWidget() {
    return Container(
      padding: EdgeInsets.fromLTRB(60, 0, 60, 0),
      child: ElevatedButton(
          child: Container(
            height: 40,
            width: double.infinity,
            alignment: Alignment.center,
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(1), color: Colors.blue),
            child: Text(
              "실행하기",
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
              textAlign: TextAlign.center,
            ),
          ),
          onPressed: () async {
            if (controller.text == 'sit') {
              Future.delayed(Duration.zero, () {
                Get.offNamed("/home", arguments: 'sit');
              });
              await DatabaseHelper.instance.add(
                Code(name: controller.text),
              );
              setState(() {
                controller.clear();
              });
            } else if (controller.text == 'gm') {
              Future.delayed(Duration.zero, () {
                Get.offNamed("/home", arguments: 'km');
              });
              await DatabaseHelper.instance.add(
                Code(name: controller.text),
              );
              setState(() {
                controller.clear();
              });
            }
            // 여기서 코드에 따라 다른 값을 넘겨주면 됨
          }),
    );
  } // 버튼

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: FutureBuilder<List<Code>>(
          future: DatabaseHelper.instance.getCodes(),
          builder: (BuildContext context, AsyncSnapshot<List<Code>> snapshot) {
            return Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    width: 1,
                    height: 1,
                    child: ListView(
                      children: snapshot.data!.map((code) {
                        if (code.name == 'sit') {
                          Future.delayed(Duration.zero, () {
                            Get.offNamed("/home", arguments: 'sit');
                          });
                        } else if (code.name == 'gm') {
                          Future.delayed(Duration.zero, () {
                            Get.offNamed("/home", arguments: 'km');
                          });
                        }
                        return Center(
                          child: Text(code.name),
                        );
                      }).toList(),
                    ),
                  ),
                  _CodeInputWidget(),
                  _ButtonWidget(),
                ]);
          },
        ),
      ),
    );
  }
}

class Code {
  final int? id;
  final String name;

  Code({this.id, required this.name});

  factory Code.fromMap(Map<String, dynamic> json) => new Code(
        id: json['id'],
        name: json['name'],
      );

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
    };
  }
}

class DatabaseHelper {
  DatabaseHelper._privateConstructor();

  static final DatabaseHelper instance = DatabaseHelper._privateConstructor();

  static Database? _database;

  Future<Database> get database async => _database ??= await _initDatabase();

  Future<Database> _initDatabase() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    String path = join(documentsDirectory.path, 'codes.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: _onCreate,
    );
  }

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
    List<Code> codeList =
        codes.isNotEmpty ? codes.map((c) => Code.fromMap(c)).toList() : [];
    return codeList;
  }

  Future<int> add(Code code) async {
    Database db = await instance.database;
    return await db.insert('codes', code.toMap());
  }

  Future<int> remove(int id) async {
    Database db = await instance.database;
    return await db.delete('codes', where: 'id = ?', whereArgs: [id]);
  }
}
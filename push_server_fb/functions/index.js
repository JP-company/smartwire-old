const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp(functions.config().firebase);
// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });
// npx eslint index.js --fix

exports.push_notification_server =
    // eslint-disable-next-line max-len
    functions.firestore.document("push_server/{mUid}").onWrite(async (change, event) =>{
      const serverData = change.after.data();
      let usercollection = "";

      if (serverData["wire"] == "wire_1" || serverData["wire"] == "wire_2") {
        usercollection =
          await admin.firestore().collection("users")
              .doc("company").collection("sit").get();
      } else {
        usercollection =
          await admin.firestore().collection("users")
              .doc("company").collection("sit").get();
      }

      let wireNum = "";

      if (serverData["wire"] == "wire_1") {
        wireNum = "1번";
      } else if (serverData["wire"] == "wire_2") {
        wireNum = "2번";
      } else if (serverData["wire"] == "KM_wire_1") {
        wireNum = "2호기";
      } else if (serverData["wire"] == "KM_wire_2") {
        wireNum = "3호기";
      } else if (serverData["wire"] == "KM_wire_3") {
        wireNum = "5호기";
      } else if (serverData["wire"] == "KM_wire_4") {
        wireNum = "6호기";
      }


      const tokens = [];
      usercollection.forEach((tokenDoc) => {
        tokens.push(tokenDoc.id);
      });
      console.log(tokens);

      let title = "";
      let body = "";
      if (serverData["push"] == "on") {
        title = "와이어 가동 알림";
        body = wireNum + " 와이어 가동이 시작되었습니다.";
      } else if (serverData["push"] == "off") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어가 정지되었습니다.";
      } else if (serverData["push"] == "nowire") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어 선이 부족합니다.";
      } else if (serverData["push"] == "contact") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어 선이 접촉중입니다.";
      } else if (serverData["push"] == "moff") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어가 M코드 정지되었습니다.";
      } else if (serverData["push"] == "finished") {
        title = "와이어 작업 완료 알림";
        body = wireNum + " 와이어 작업이 완료되었습니다.";
      } else if (serverData["push"] == "uncut") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어 선이 씹혔습니다.";
      } else if (serverData["push"] == "pause") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어가 미동작입니다.";
      } else if (serverData["push"] == "exit") {
        title = "오류 알림";
        body = wireNum +
        " 와이어 알림 프로그램이 종료되었습니다. \n와이어 기계상에 있는 알림 프로그램을 실행시켜주세요.";
      }

      const options = {
        priority: "high",
      };

      const payload = {
        notification: {
          title: title,
          body: body,
          sound: "default",
        },
      };

      await admin.messaging().sendToDevice(tokens, payload, options)
          .then(function(response) {
            console.log("알림 보내기 성공", response);
          }).catch(function(error) {
            console.log("알림 오류 발생", error);
          });
    });

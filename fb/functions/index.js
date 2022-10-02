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


exports.sit_1=
    // eslint-disable-next-line max-len
    functions.firestore.document("wire_1/dates/time/{mUid}").onWrite(async (change, event) =>{
      const usercollection =
      await admin.firestore().collection("users")
          .doc("company").collection("sit").get();

      const onoff = change.after.data();
      let title = "";
      let body = "";
      if (onoff["push"] == "on") {
        title = "와이어 가동 알림";
        body = "1번 와이어 가동이 시작되었습니다.";
      } else if (onoff["push"] == "off") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 정지되었습니다.";
      } else if (onoff["push"] == "uncut") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 씹혔습니다.";
      } else if (onoff["push"] == "nowire") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 부족합니다.";
      } else if (onoff["push"] == "contact") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 접촉중입니다.";
      } else if (onoff["push"] == "pause") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 미동작입니다.";
      } else if (onoff["push"] == "moff") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 M코드 정지되었습니다.";
      } else if (onoff["push"] == "finished") {
        title = "와이어 작업 완료 알림";
        body = "1번 와이어 작업이 완료되었습니다.";
      } else if (onoff["push"] == "exit") {
        title = "오류 알림";
        body = "알림 프로그램이 종료되었습니다. 와이어 기계상에 있는 알림 프로그램을 실행시켜주세요.";
      }

      console.log(onoff);

      const tokens = [];
      usercollection.forEach((tokenDoc) => {
        tokens.push(tokenDoc.id);
      });
      console.log(tokens);

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

      await admin.messaging().sendToDevice(tokens, payload, options);
    });

exports.sit_2=
    // eslint-disable-next-line max-len
    functions.firestore.document("wire_2/dates/time/{mUid}").onWrite(async (change, event) =>{
      const usercollection =
      await admin.firestore().collection("users")
          .doc("company").collection("sit").get();

      const onoff = change.after.data();
      let title = "";
      let body = "";
      if (onoff["push"] == "on") {
        title = "와이어 가동 알림";
        body = "1번 와이어 가동이 시작되었습니다.";
      } else if (onoff["push"] == "off") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 정지되었습니다.";
      } else if (onoff["push"] == "uncut") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 씹혔습니다.";
      } else if (onoff["push"] == "nowire") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 부족합니다.";
      } else if (onoff["push"] == "contact") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 접촉중입니다.";
      } else if (onoff["push"] == "pause") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 미동작입니다.";
      } else if (onoff["push"] == "moff") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 M코드 정지되었습니다.";
      } else if (onoff["push"] == "finished") {
        title = "와이어 작업 완료 알림";
        body = "1번 와이어 작업이 완료되었습니다.";
      } else if (onoff["push"] == "exit") {
        title = "오류 알림";
        body = "알림 프로그램이 종료되었습니다. 와이어 기계상에 있는 알림 프로그램을 실행시켜주세요.";
      }

      const tokens = [];
      usercollection.forEach((tokenDoc) => {
        tokens.push(tokenDoc.id);
      });
      console.log(tokens);

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

      await admin.messaging().sendToDevice(tokens, payload, options);
    });


exports.km_1=
    // eslint-disable-next-line max-len
    functions.firestore.document("KM_wire_1/dates/time/{mUid}").onWrite(async (change, event) =>{
      const usercollection =
      await admin.firestore().collection("users")
          .doc("company").collection("km").get();

      const onoff = change.after.data();
      let title = "";
      let body = "";
      if (onoff["push"] == "on") {
        title = "와이어 가동 알림";
        body = "1번 와이어 가동이 시작되었습니다.";
      } else if (onoff["push"] == "off") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 정지되었습니다.";
      } else if (onoff["push"] == "nowire") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 부족합니다.";
      } else if (onoff["push"] == "contact") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 접촉중입니다.";
      } else if (onoff["push"] == "moff") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 M코드 정지되었습니다.";
      } else if (onoff["psuh"] == "finished") {
        title = "와이어 작업 완료 알림";
        body = "1번 와이어 작업이 완료되었습니다.";
      } else if (onoff["push"] == "exit") {
        title = "오류 알림";
        body = "알림 프로그램이 종료되었습니다. 와이어 기계상에 있는 알림 프로그램을 실행시켜주세요.";
      }

      const tokens = [];
      usercollection.forEach((tokenDoc) => {
        tokens.push(tokenDoc.id);
      });
      console.log(tokens);

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

      await admin.messaging().sendToDevice(tokens, payload, options);
    });


exports.km_2=
    // eslint-disable-next-line max-len
    functions.firestore.document("KM_wire_2/dates/time/{mUid}").onWrite(async (change, event) =>{
      const usercollection =
      await admin.firestore().collection("users")
          .doc("company").collection("km").get();

      const onoff = change.after.data();
      let title = "";
      let body = "";
      if (onoff["push"] == "on") {
        title = "와이어 가동 알림";
        body = "1번 와이어 가동이 시작되었습니다.";
      } else if (onoff["push"] == "off") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 정지되었습니다.";
      } else if (onoff["push"] == "nowire") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 부족합니다.";
      } else if (onoff["push"] == "contact") {
        title = "와이어 정지 알림";
        body = "1번 와이어 선이 접촉중입니다.";
      } else if (onoff["push"] == "moff") {
        title = "와이어 정지 알림";
        body = "1번 와이어가 M코드 정지되었습니다.";
      } else if (onoff["push"] == "finished") {
        title = "와이어 작업 완료 알림";
        body = "1번 와이어 작업이 완료되었습니다.";
      } else if (onoff["push"] == "exit") {
        title = "오류 알림";
        body = "알림 프로그램이 종료되었습니다. 와이어 기계상에 있는 알림 프로그램을 실행시켜주세요.";
      }

      const tokens = [];
      usercollection.forEach((tokenDoc) => {
        tokens.push(tokenDoc.id);
      });
      console.log(tokens);

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

      await admin.messaging().sendToDevice(tokens, payload, options);
    });

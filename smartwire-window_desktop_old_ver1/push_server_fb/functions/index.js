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
              .doc("company").collection("km").get();
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
      if (serverData["push"] == "stop_contact") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어 접촉";
      } else if (serverData["push"] == "stop_contact_30s") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어 30초 접촉";
      } else if (serverData["push"] == "stop_moff") {
        title = "와이어 정지 알림";
        body = wireNum + " M코드 정지";
      } else if (serverData["push"] == "stop_cut") {
        title = "와이어 정지 알림";
        body = wireNum + " 작업중 와이어 단선";
      } else if (serverData["push"] == "stop_insert_failure") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동결선 삽입실패(M20)";
      } else if (serverData["push"] == "stop_cut_failure") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동결선 절단실패(M21)";
      } else if (serverData["push"] == "stop_cleanup_failure") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동결선 잔여와이어 처리실패(M21)";
      } else if (serverData["push"] == "stop_wire_notworking") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어 미동작";
      } else if (serverData["push"] == "stop_liquid_notworking") {
        title = "와이어 정지 알림";
        body = wireNum + " 가공액 미동작";
      } else if (serverData["push"] == "stop_feed_motor_alarm") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동결선 FEED MOTOR ALARM!!";
      } else if (serverData["push"] == "stop_auto_cut_failure") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동결선 절단 공정 실패";
      } else if (serverData["push"] == "stop_auto_cleanup_failure") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동결선 잔여와이어 처리 실패";
      } else if (serverData["push"] == "stop_lowerpart_contact") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동결선 하부 뭉치 WIRE CONTACT";
      } else if (serverData["push"] == "stop_awf_sensor") {
        title = "와이어 정지 알림";
        body = wireNum + " AWF 명령끝날때까지 센서감지 안됨";
      } else if (serverData["push"] == "stop_fluid_sensor") {
        title = "와이어 정지 알림";
        body = wireNum + " 오일센서 이상 감지";
      } else if (serverData["push"] == "stop_door_sensor") {
        title = "와이어 정지 알림";
        body = wireNum + " 자동문센서 이상 감지";
      } else if (serverData["push"] == "stop_collect_breakaway") {
        title = "와이어 정지 알림";
        body = wireNum + " 회수부 와이어 이탈";
      } else if (serverData["push"] == "ready_on") {
        title = "와이어 정지 알림";
        body = wireNum + " Ready On";
      } else if (serverData["push"] == "stop_emergency") {
        title = "와이어 정지 알림";
        body = wireNum + " 비상정지";
      } else if (serverData["push"] == "ready_off") {
        title = "와이어 정지 알림";
        body = wireNum + " READY Off";
      } else if (serverData["push"] == "stop_reset") {
        title = "와이어 정지 알림";
        body = wireNum + " 리셋";
      } else if (serverData["push"] == "stop_finished") {
        title = "작업 완료 알림";
        body = wireNum + " 작업이 완료되었습니다.";
      } else if (serverData["push"] == "stop") {
        title = "와이어 정지 알림";
        body = wireNum + " 와이어가 정지되었습니다.";
      } else if (serverData["push"] == "start_autostart") {
        title = "와이어 가동 알림";
        body = wireNum + " 자동 재시작 프로그램을 실행하였습니다.";
      } else if (serverData["push"] == "start_restart") {
        title = "와이어 가동 알림";
        body = wireNum + " 가공 재시작";
      } else if (serverData["push"] == "start") {
        title = "와이어 가동 알림";
        body = wireNum + " 작업 시작";
      } else if (serverData["push"] == "Initialization") {
        title = "와이어 알림";
        body = wireNum + " 와이어 기계 연결 완료";
      } else if (serverData["push"] == "stop_closed") {
        title = "와이어 알림";
        body = wireNum + " 와이어 기계 전원 종료됨";
      } else if (serverData["push"] == "stop_disconnected") {
        title = "와이어 알림";
        body = wireNum + " 와이어 기계 연결 끊어짐";
      } else if (serverData["push"] == "stop_open_succeeded") {
        title = "와이어 알림";
        body = wireNum + " 와이어 기계 전원 켜짐";
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

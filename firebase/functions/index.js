const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

exports.sit_1_a =
    // eslint-disable-next-line max-len
    functions.firestore.document('wire_1/dates/time/{mUid}').onWrite(async (event) =>{
      const userDoc = await admin.firestore().doc('users/1').get();
      const fcmToken = userDoc.get('token');

      const message = {
        notification: {
          title: '와이어 가동 알림',
          body: '1번 와이어 작동 상태가 변경되었습니다.',
        },
        token: fcmToken,
      };

      await admin.messaging().send(message).then((response) => {
        console.log(response);
      });
    });

exports.sit_1_b =
    // eslint-disable-next-line max-len
    functions.firestore.document('wire_2/dates/time/{mUid}').onWrite(async (event) =>{
      const userDoc = await admin.firestore().doc('users/1').get();
      const fcmToken = userDoc.get('token');

      const message = {
        notification: {
          title: '와이어 가동 알림',
          body: '2번 와이어 작동 상태가 변경되었습니다.',
        },
        token: fcmToken,
      };

      await admin.messaging().send(message).then((response) => {
        console.log(response);
      });
    });

exports.sit_2_a =
    // eslint-disable-next-line max-len
    functions.firestore.document('wire_1/dates/time/{mUid}').onWrite(async (event) =>{
      const userDoc = await admin.firestore().doc('users/2').get();
      const fcmToken = userDoc.get('token');

      const message = {
        notification: {
          title: '와이어 가동 알림',
          body: '1번 와이어 작동 상태가 변경되었습니다.',
        },
        token: fcmToken,
      };

      await admin.messaging().send(message).then((response) => {
        console.log(response);
      });
    });

exports.sit_2_b =
    // eslint-disable-next-line max-len
    functions.firestore.document('wire_2/dates/time/{mUid}').onWrite(async (event) =>{
      const userDoc = await admin.firestore().doc('users/2').get();
      const fcmToken = userDoc.get('token');

      const message = {
        notification: {
          title: '와이어 가동 알림',
          body: '2번 와이어 작동 상태가 변경되었습니다.',
        },
        token: fcmToken,
      };

      await admin.messaging().send(message).then((response) => {
        console.log(response);
      });
    });

exports.sit_3_a =
    // eslint-disable-next-line max-len
    functions.firestore.document('wire_1/dates/time/{mUid}').onWrite(async (event) =>{
      const userDoc = await admin.firestore().doc('users/3').get();
      const fcmToken = userDoc.get('token');

      const message = {
        notification: {
          title: '와이어 가동 알림',
          body: '1번 와이어 작동 상태가 변경되었습니다.',
        },
        token: fcmToken,
      };

      await admin.messaging().send(message).then((response) => {
        console.log(response);
      });
    });

exports.sit_3_b =
    // eslint-disable-next-line max-len
    functions.firestore.document('wire_2/dates/time/{mUid}').onWrite(async (event) =>{
      const userDoc = await admin.firestore().doc('users/3').get();
      const fcmToken = userDoc.get('token');

      const message = {
        notification: {
          title: '와이어 가동 알림',
          body: '2번 와이어 작동 상태가 변경되었습니다.',
        },
        token: fcmToken,
      };

      await admin.messaging().send(message).then((response) => {
        console.log(response);
      });
    });

class Memo {
  final int id;
  final String code;

  Memo({required this.id, required this.code});

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'code': code,
    };
  }

  // 각 memo 정보를 보기 쉽도록 print 문을 사용하여 toString을 구현하세요
  @override
  String toString() {
    return 'Memo{id: $id, code: $code}';
  }
}
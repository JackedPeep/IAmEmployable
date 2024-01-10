List<dynamic>? flatten(List? list) {
  if (list == null) {
    return null;
  }
  List<dynamic> result = [];
  for (var sublist in list) {
    if (sublist != null) {
      for (var item in sublist) {
        if (item != null) {
          result.add(item);
        }
      }
    }
  }
  return result;
}

List<dynamic>? deepen(List<dynamic>? list) {
  if (list == null) {
    return null;
  }
  if (list.isEmpty) {
    return [];
  }
  List<dynamic> result = [list[0]];
  List<dynamic> current = result;
  for (int i = 1; i < list.length; i++) {
    current.add([list[i]]);
    current = current[1];
  }
  return result;
}


Stream<int> Function() fibonnaciNumbers(int n) {
  return (() async* {
    int a = 0;
    int b = 1;
    yield a;
    yield b;
    for (int i = 2; i < n; i++) {
      int c = a + b;
      yield c;
      a = b;
      b = c;
    }
  });
}

Stream<int> Function() streamFilter(Stream<int> stream, bool Function(int) filterFunction) {
  return (() async* {
    await for (int number in stream) {
      if (filterFunction(number)) {
        yield number;
      }
    }
  });
}

Stream<int> Function() streamAccumulate(Stream<int> stream, int Function(int, int) f, int initial) {
  return (() async* {
    int acc = initial;
    await for (int number in stream) {
      acc = f(acc, number);
      yield acc;
    }
  });
}
Stream<int> generateNumbers(int n) async* {
  for (int i = 1; i <= n; i++) {
    await Future<void>.delayed(const Duration(seconds: 1));
    yield i;
  }
}

void main(List<String> arguments) async {
  print( 'flattening [[0,1], [2]] yields ${flatten([[0,1], [2]])}');
  print( 'flattening [[0,1], [2], null] yields ${flatten([[0,1], [2], null])}');
  print( 'flattening [[0,1, null], [2]] yields ${flatten([[0,1, null], [2]])}');
  print( 'flattening null yields ${flatten(null)}');
  print( 'flattening [null] yields ${flatten([null])}');
  print( 'deepening [0,1,2] yields ${deepen([0,1,2])}');
  print( 'deepening [0,null,2] yields ${deepen([0,null,2])}');
  print( 'deepening [0] yields ${deepen([0])}');
  print( 'deepening [] yields ${deepen([])}');
  print( 'deepening null yields ${deepen(null)}');
  
  await for (final number in fibonnaciNumbers(7)()) {
    print ('fibonnaci number is $number');
  }
 await for (final number in streamFilter(generateNumbers(10), ((a) {return a % 2 == 0;}))()) {
    print ('filtered number is $number');
}

await for (final number in streamAccumulate(generateNumbers(10),((a,b) {return a+b;}),0)()) {
    print ('cumulative number is $number.');
}

}

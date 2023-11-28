Stream<int> Function() fibonnaciNumbers(int n) {

}                                        

Stream<int> Function() streamFilter(Stream<int> stream, bool Function(int) f) {

}                                        

Stream<int> Function() streamAccumulation(Stream<int> stream, int Function(int, int) f, initial) {

} 

Stream<int> Function() generateNumbers(int n) {
  final Stream<int> Function() func = (() async* {
    for (int i = 1; i <= n; i++) {
      await Future<void>.delayed(const Duration(seconds: 1));
        yield i;
      }
    });
  return func;
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
    print ('fibonnaci number is ${number}')
  }
  await for (final number in streamFilter(generateNumbers(10)(), ((a) {return a % 2 == 0;}))()) {
    print ('filtered number is $number');
  }
 
  await for (final number in streamAccumulation(generateNumbers(10)(),((a,b) {return a+b;}),0)()) {
      print ('cumulative number is $number.');
  }  
}


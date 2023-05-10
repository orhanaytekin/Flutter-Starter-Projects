import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import "dart:io";
import 'package:liquid_swipe/liquid_swipe.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final ImagePicker _picker = ImagePicker();
  final XFile file = XFile("assets/indir.jpeg");
  List<XFile>? _imageFileList = [];
  List<Widget>? keep_these = [];
  List<Widget> warHero = [];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("COMPILATION")),
      drawer: Drawer(
        child: ListView(
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
              child: Text('Drawer Header'),
            ),
            OutlinedButton(
              child: const Text("Add Image(s)"),
              onPressed: () {
                selectImages();
              },
            ),
            OutlinedButton(
              child: const Text("List Image(s) Here"),
              onPressed: () {
                setState(() {});
              },
            ),
            OutlinedButton(
              child: const Text("Swipe Page"),
              onPressed: () async {
                if (keep_these!.isEmpty) {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                    behavior: SnackBarBehavior.floating,
                    content: Container(
                      padding: const EdgeInsets.all(8),
                      height: 70,
                      decoration: const BoxDecoration(
                        color: Colors.blue,
                        borderRadius: BorderRadius.all(Radius.circular(15)),
                      ),
                      child: const Center(
                        child: Text('There is no image selected.'),
                      ),
                    ),
                  ));
                } else {
                  //fuckin_wait(widgets);
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (BuildContext context) {
                        print(keep_these!.length);

                        return NewLiq(keepThese: keep_these!);
                      },
                    ),
                  );
                }
                setState(() {
                  // List<Widget> widgets = [];
                  // widgets.addAll(keep_these!);
                  // keep_these!.clear();
                });
              },
            ),
            OutlinedButton(
              child: const Text("Clear"),
              onPressed: () {
                _imageFileList!.clear();
                keep_these!.clear();
                setState(() {});
              },
            ),
          ],
        ),
      ),
      body: Stack(
        children: [
          SafeArea(
            child: Column(
              children: [
                // OutlinedButton(
                //   child: const Text("Add Image(s)"),
                //   onPressed: () {
                //     selectImages();
                //   },
                // ),
                // OutlinedButton(
                //   child: const Text("List Image(s) Here"),
                //   onPressed: () {
                //     setState(() {});
                //   },
                // ),

                // OutlinedButton(
                //   child: const Text(" Swipe Page"),
                //   onPressed: () {
                //     setState(() {});
                //     List<Widget> widgets = [];
                //     widgets.addAll(keep_these!);
                //     keep_these!.clear();
                //     if (widgets.isEmpty) {
                //       ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                //         behavior: SnackBarBehavior.floating,
                //         content: Container(
                //           padding: const EdgeInsets.all(8),
                //           height: 70,
                //           decoration: const BoxDecoration(
                //             color: Colors.blue,
                //             borderRadius: BorderRadius.all(Radius.circular(15)),
                //           ),
                //           child: const Center(
                //             child: Text('There is no image selected.'),
                //           ),
                //         ),
                //       ));
                //     } else {
                //       //fuckin_wait(widgets);
                //       Navigator.push(
                //         context,
                //         MaterialPageRoute(
                //           builder: (BuildContext context) {
                //             print(keep_these!.length);

                //             return NewLiq(keepThese: widgets);
                //           },
                //         ),
                //       );
                //     }
                //   },
                // ),
                // OutlinedButton(
                //   child: const Text("Clear"),
                //   onPressed: () {
                //     _imageFileList!.clear();
                //     keep_these!.clear();
                //     setState(() {});
                //   },
                // ),
                // const SizedBox(height: 50, child: Text("313132131")),

                Expanded(
                  child: Stack(
                    children: [
                      GridView.builder(
                        itemCount: _imageFileList!.length,
                        gridDelegate:
                            const SliverGridDelegateWithFixedCrossAxisCount(
                          crossAxisCount: 2,
                        ),
                        itemBuilder: (BuildContext context, int index) {
                          print(
                              "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
                          // return const SizedBox();
                          return buildPage(
                            file: File(_imageFileList![index].path),
                            assetType: " ",
                            title: "How you doin ",
                            subtitle: "Good wbu",
                          );

                          // return Image.file(
                          //   File(_imageFileList![index].path),
                          //   fit: BoxFit.cover,
                          // );
                        },
                      ),
                      // const Text("abiiii"),

                      LiquidSwipe.builder(
                        itemBuilder: (BuildContext context, int index) {
                          Widget wbu = buildPage(
                            file: File(_imageFileList![index - 1].path),
                            assetType: " ",
                            title: "Hello ",
                            subtitle: "Good wbu",
                          );
                          if (!keep_these!.contains(wbu)) {
                            keep_these!.add(wbu);
                          }
                          print(
                              "${keep_these!.length} AKLKSFŞLKOPCKŞAÖCŞÖCŞSLCAÇŞSCŞÇ");
                          return const SizedBox(
                            height: 0,
                            width: 0,
                          );
                        },
                        itemCount: _imageFileList!.length + 1,
                      )
                    ],
                  ),
                ),
                // LiquidSwipe.builder(
                //     enableSideReveal: true,
                //     slideIconWidget: const Icon(
                //       Icons.arrow_back_ios,
                //       color: Colors.white,
                //     ),
                //     itemCount: 1,
                //     itemBuilder: (context, index) {
                //       File file = File(_imageFileList![index - 1].path);
                //       return buildPage(
                //         file: file,
                //       );
                //     }),
              ],
            ),
          ),
          //fuckin_wait(),
        ],
      ),
    );
  }

  // @override
  // void initState() {
  //   super.initState();
  // }

  // void wait(int i) {
  //   Future.delayed(Duration(seconds: i));
  // }

  void selectImages() async {
    final List<XFile>? selectedImages = await _picker.pickMultiImage();
    if (selectedImages!.isNotEmpty) {
      _imageFileList!.addAll(selectedImages);
    }

    print("Image List Length: ${_imageFileList!.length}");
  }

  Future<int> myFunc() async {
    while (_imageFileList!.isEmpty) {
      await Future.delayed(const Duration(seconds: 3));
    }
    return Future.value(_imageFileList!.length);
  }

  Future<int?> convert() async {
    int? a = await myFunc();
    return a;
  }

  Widget buildPage({
    required File file,
    required String assetType,
    String path = " ",
    String title = " ",
    String subtitle = " ",
  }) {
    return Container(
      color: Colors.red,
      padding: const EdgeInsets.all(24),
      child: ListView(
        children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              assetType == "asset"
                  ? Image.asset(
                      path,
                      fit: BoxFit.cover,
                      width: double.infinity,
                    )
                  : Image.file(
                      file,
                      fit: BoxFit.fitHeight,
                      width: double.infinity,
                    ),
              const SizedBox(height: 64),
              Text(
                title,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 46,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 24),
              Container(
                padding: const EdgeInsets.only(right: 32),
                // child: const TextField(
                //     obscureText: true,
                //     decoration: InputDecoration(
                //       border: OutlineInputBorder(),
                //       labelText: 'Password',
                //     )),
                child: Text(
                  subtitle,
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  fuckin_wait(keepThese) {
    LiquidSwipe(
      //ignoreUserGestureWhileAnimating: true,
      enableSideReveal: true,
      slideIconWidget: const Icon(
        Icons.arrow_back_ios,
      ),
      pages: keepThese,
    );
  }
}

class NewPage extends StatelessWidget {
  NewPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Next Page")),
      body: Container(
          alignment: Alignment.topCenter,
          // padding: EdgeInsets.all(30),
          child: Column(
            children: [
              ElevatedButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: Text("Go Back"),
              ),
            ],
          )),
    );
  }
}

class NewLiq extends StatelessWidget {
  List<Widget> keepThese;
  NewLiq({Key? key, required this.keepThese}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Next Page"),
        actions: [
          ElevatedButton(
            onPressed: () {
              Navigator.pop(context);
            },
            child: const Text("Go Back"),
          ),
        ],
      ),
      body: LiquidSwipe(
        ignoreUserGestureWhileAnimating: true,
        enableSideReveal: true,
        slideIconWidget: const Icon(
          Icons.arrow_back_ios,
        ),
        pages: keepThese,
      ),
    );
  }
}

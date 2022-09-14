import 'dart:io';
import 'dart:math' as math;
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import "main.dart";
import "globals.dart";
import "package:liquid_swipe/liquid_swipe.dart";
import 'list_photos.dart';

// class LiquidView extends StatelessWidget {
//   const LiquidView({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text("LIQUID SWIPE"),
//       ),
//     );
//   }
// }

class LiquidView extends StatefulWidget {
  List<XFile>? imageList = MyHomePage.imageFileList;
  LiquidView({Key? key}) : super(key: key);

  @override
  State<LiquidView> createState() => LiquidViewState();
}

class LiquidViewState extends State<LiquidView> {
  List<Widget> widgets = [];
  @override
  Widget build(BuildContext context) {
    for (int i = 0; i < widget.imageList!.length; i++) {
      File file = File(widget.imageList![i].path);
      widgets.add(
        showImages("file", "", file, i),
      );
    }
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        appBarTheme: const AppBarTheme(
          color: Colors.transparent,
        ),
        scaffoldBackgroundColor:
            Globals.selected == false ? Colors.blueAccent : Colors.black,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            'Slide',
            style: TextStyle(
              color: Globals.selected == false ? Colors.black : Colors.red,
            ),
          ),
          leading: IconButton(
            onPressed: () {
              Navigator.pop(context);
            },
            icon: const Icon(Icons.arrow_back),
            color: Globals.selected == false ? Colors.black : Colors.red,
          ),
          actions: [
            IconButton(
              color: Globals.selected == false ? Colors.black : Colors.red,
              onPressed: () {
                Navigator.popAndPushNamed(context, '/');
              },
              icon: const Icon(Icons.clear),
            ),
          ],
        ),
        body: widgets.isNotEmpty
            ? LiquidSwipe(
                ignoreUserGestureWhileAnimating: true,
                enableSideReveal: true,
                slideIconWidget: const Icon(
                  Icons.arrow_back_ios,
                ),
                pages: widgets,
              )
            : Column(
                children: [
                  SizedBox(
                    child: Globals.selected == false
                        ? Image.asset("assets/gifs/searching.gif",
                            fit: BoxFit.cover)
                        : Image.asset("assets/gifs/scared.gif"),
                  ),
                  Center(
                    child: ElevatedButton(
                      onPressed: () {
                        Navigator.pop(context);
                      },
                      child: Center(
                        child: FittedBox(
                          child: Globals.selected == false
                              ? const Text(
                                  "We searched but there is not any selected image! \n Click here to go back.",
                                  style: TextStyle(
                                    color: Colors.black,
                                  ),
                                )
                              : const Text(
                                  "Sorry, we couldn't find any selected image at this time!\nClick here to go back.",
                                  style: TextStyle(color: Colors.red)),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
      ),
    );
  }

  Widget showImages(
    String type,
    String filePath,
    File file,
    int a,
  ) {
    return Container(
      color: Color((math.Random().nextDouble() * 0xFFFFFF).toInt())
          .withOpacity(1.0),
      // fit: StackFit.expand,
      // clipBehavior: Clip.antiAliasWithSaveLayer,
      // crossAxisAlignment: CrossAxisAlignment.start,
      // mainAxisAlignment: MainAxisAlignment.center,
      alignment: Alignment.center,
      child: type == "asset"
          ? Image.asset(
              filePath,
              height: MediaQuery.of(context).size.height * 0.9,
              width: MediaQuery.of(context).size.width * 0.9,
              fit: BoxFit.cover,
              //fit: BoxFit.cover,
              //width: double.infinity,
            )
          : Image.file(
              height: MediaQuery.of(context).size.height * 0.8,
              width: MediaQuery.of(context).size.width * 0.8,
              // height: MediaQuery.of(context).size.height - 150, real ones
              // width: MediaQuery.of(context).size.width,
              fit: BoxFit.cover,
              file,
              //fit: BoxFit.fitHeight,
              //width: double.infinity,
            ),
      // const SizedBox(height: 64),
      // const Text(
      //   "title",
      //   style: TextStyle(
      //     color: Colors.white,
      //     fontSize: 46,
      //     fontWeight: FontWeight.bold,
      //   ),
      // ),
      // const SizedBox(height: 24),
      // Container(
      //   padding: const EdgeInsets.only(right: 32),
      // child: const TextField(
      //     obscureText: true,
      //     decoration: InputDecoration(
      //       border: OutlineInputBorder(),
      //       labelText: 'Password',
      //     )),
      // child: const Text(
      //   "subtitle",
      //   style: TextStyle(
      //     color: Colors.white,
      //     fontSize: 20,
      //   ),
      // ),
      // ),
    );
  }
}

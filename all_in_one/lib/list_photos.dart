import 'dart:io';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/material.dart';
import 'main.dart';
import 'globals.dart';
import 'package:image_picker/image_picker.dart';
import 'package:flutter_svg/flutter_svg.dart';

class ListPhotos extends StatelessWidget {
  const ListPhotos({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _ListPhotos(),
      // appBar: AppBar(),
    );
  }
}

// ignore: must_be_immutable
class _ListPhotos extends StatefulWidget {
  List<XFile>? imageList = MyHomePage.imageFileList;
  _ListPhotos({Key? key}) : super(key: key);

  @override
  State<_ListPhotos> createState() => ListPhotosState();
}

class ListPhotosState extends State<_ListPhotos> {
  List<Widget> widgets = [];
  @override
  Widget build(BuildContext context) {
    print("${widget.imageList!.length} okLJCMAJSLVAÖŞSÖVLAŞVÖ");

    for (int i = 0; i < widget.imageList!.length; i++) {
      File file = File(widget.imageList![i].path);
      widgets.add(showImages("file", "", file));
    }
    // GridView.builder(
    //   itemCount: imageList!.length,
    //   gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
    //       crossAxisCount: 3, childAspectRatio: 3.0 / 4.6),
    //   itemBuilder: (context, index) {
    //     print("${imageList!.length} okLJCMAJSLVAÖŞSÖVLAŞVÖ");
    //     File file = File(imageList![index].path);
    //     String name = file.path.split('/').last;

    //     // return ListView(children: [showImages("file", "", file)]);
    //     return const SizedBox();
    //   },
    // );
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
        // shrinkWrap: false,
        // reverse: false, //starts from start/end of the list
        appBar: AppBar(
          leading: IconButton(
            onPressed: () {
              Navigator.pop(context);
            },
            icon: const Icon(Icons.arrow_back),
            color: Globals.selected == false ? Colors.black : Colors.red,
          ),
          iconTheme: IconThemeData(
              color: Globals.selected == false ? Colors.black : Colors.red),
          title: Text(
            "List Photos",
            style: TextStyle(
              color: Globals.selected == false ? Colors.black : Colors.red,
            ),
          ),
          backgroundColor:
              Globals.selected == false ? Colors.blue : Colors.black,
          actions: [
            IconButton(
              onPressed: () {
                Navigator.popAndPushNamed(context, '/');
              },
              icon: const Icon(Icons.clear),
            ),
          ],
        ),
        body: widgets.isNotEmpty
            ? ListView(
                children: widgets,
              )
            : Column(
                children: [
                  SizedBox(
                    // width: MediaQuery.of(context).size.width,
                    // height: MediaQuery.of(context).size.height,
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
                                    "We searched but there is not any selected image!\nClick here to go back.",
                                    style: TextStyle(
                                      color: Colors.black,
                                    ),
                                  )
                                : const Text(
                                    "Sorry, we couldn't find any selected image at this time!\nClick here to go back.",
                                    style: TextStyle(color: Colors.red))),
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
  ) {
    return Container(
      child: type == "asset"
          ? Image.asset(
              height: MediaQuery.of(context).size.height,
              width: MediaQuery.of(context).size.width,
              fit: BoxFit.cover,
              filePath,
            )
          : Image.file(
              height: MediaQuery.of(context).size.height,
              width: MediaQuery.of(context).size.width,
              fit: BoxFit.cover,
              file),
    );
  }
}

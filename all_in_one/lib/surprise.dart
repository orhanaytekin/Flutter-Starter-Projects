import 'package:flutter/material.dart';
import "globals.dart";
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';

class Surprise extends StatefulWidget {
  const Surprise({Key? key}) : super(key: key);

  @override
  State<Surprise> createState() => _SurpriseState();
}

class _SurpriseState extends State<Surprise> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: const Icon(Icons.arrow_back),
          color: Colors.white,
        ),
        actions: [
          IconButton(
            color: Colors.white,
            onPressed: () {
              Navigator.popAndPushNamed(context, '/');
            },
            icon: const Icon(Icons.clear),
          ),
        ],
        backgroundColor: const Color.fromARGB(255, 45, 1, 53),
        title: Center(
            child: Globals.selected == false
                ? const Text("ÖZGE")
                : const Text("PLANKTON")),
      ),
      body: Globals.selected == false
          ? Image.asset(
              "assets/light_mode/reyna.jpg",
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              fit: BoxFit.fill,
            )
          : Image.asset(
              "assets/gifs/plankton.gif",
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              fit: BoxFit.fill,
            ),
    );
  }
}

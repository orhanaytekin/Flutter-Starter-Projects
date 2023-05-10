import 'package:flutter/material.dart';
import 'package:testproject/models/worker.dart';

void main() => runApp(myApp());

class myApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        cardColor: const Color.fromRGBO(156, 39, 176, 1),
        primaryColor: const Color.fromARGB(255, 1, 1, 1),
        brightness: Brightness.light,
        primaryColorDark: Colors.yellow,
        primaryColorLight: Colors.black,
      ),
      debugShowCheckedModeBanner: false,
      home: HomeScreen(),);
  }
}

class HomeScreen extends StatelessWidget{

  List<Worker> workers = [Worker("Orhan","Aytekin",1650),Worker.withId(48, "ahmet", "çakar", 5500),Worker("Mert","Karahan",50)];

  @override
  Widget build(BuildContext context) {

    for(var i = 0; i <workers.length; i++){
      Worker worker = workers[i];

    }

    return Scaffold(
        body: Stack(children: [Container( decoration: const BoxDecoration(image: DecorationImage(image: AssetImage("assets/indir.jpeg"),fit: BoxFit.cover,
        colorFilter: ColorFilter.mode(Colors.white , BlendMode.darken),
        
        ))),buildBody(),],) ,
        backgroundColor: const Color.fromARGB(255, 0, 0, 0),
        appBar: AppBar(
          backgroundColor: Colors.black,
          title: const Center(
            child : Text("ANKARA SU VE KANALİZASYON İŞLERİ",
              style: TextStyle(color: Colors.white),
            ),
          ),
        )
    );
  }


  Widget buildBody() {
    return Column(
      children: <Widget>[
        Expanded(
          child: ListView.builder(
            itemCount: workers.length,
            itemBuilder: (BuildContext context,int index){
              return ListTile(

                  trailing: buildStatusIcon(workers[index].wage),
                  title: Text("${workers[index].name}  ${workers[index].lastName}",
                  style: TextStyle(color: Colors.white),),
                  subtitle: Text("ALDIĞI MAAŞ  "+ workers[index].wage.toString() + " "+ workers[index].getStatus.toString(),
                  style: TextStyle(color: Colors.white),),
                  leading: const CircleAvatar(
                    backgroundImage: AssetImage("assets/indir.jpeg"),

                  ));  },
          ),
        )
      ],
    );

  }

  Widget buildStatusIcon(int wage) {
    if(wage>=5500){
      return Icon(Icons.done, color: Colors.green);
    }else if(wage>=1650){
      return Icon(Icons.camera,color: Colors.amber);
    }
      return Icon(Icons.clear,color: Colors.red,);
  }

}

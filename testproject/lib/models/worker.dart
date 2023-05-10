
class Worker{
  int? id;
  String name;
  String lastName;
  int wage;
  String? status;

  Worker(this.name, this.lastName, this.wage);

  Worker.withId( this.id, this.name, this.lastName, this.wage);

  String? get getStatus{
    String message = "";
    if(wage>=5500){
      message = "Bilgisayar Mühendisi";
    }else if(wage>=1650){
      message = "Stajyer";
    }else{message = "Valorant Danışmanı";}
    status = message;
    return status;
  }
}
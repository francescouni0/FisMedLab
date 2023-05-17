
#include "G4Timer.hh"

#include "LabRunAction.hh"

#include "G4Run.hh"

LabRunAction::LabRunAction(LabInfo *info_)
 : G4UserRunAction(),
   fTimer(0){
    info = info_;
    fTimer = new G4Timer;
    
}



LabRunAction::~LabRunAction(){
  delete fTimer;
}



void LabRunAction::BeginOfRunAction(const G4Run*){
  //G4cout << "### Run " << aRun->GetRunID() << " start." << G4endl;
  fTimer->Start();
}



void LabRunAction::EndOfRunAction(const G4Run*){
  fTimer->Stop();
  //G4cout << "number of event = " << aRun->GetNumberOfEvent()
         //<< " " << *fTimer << G4endl;
  
  info->timer[0] = fTimer->GetRealElapsed();
  info->timer[1] = fTimer->GetSystemElapsed();
  info->timer[2] = info->timer[2] + fTimer->GetUserElapsed();
}



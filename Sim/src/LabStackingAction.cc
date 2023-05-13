
#include "LabStackingAction.hh"

#include "G4VProcess.hh"

#include "G4ParticleDefinition.hh"
#include "G4ParticleTypes.hh"
#include "G4SystemOfUnits.hh"
#include "G4Track.hh"
#include "G4ios.hh"
#include "G4UnitsTable.hh"

LabStackingAction::LabStackingAction(LabInfo *info_) : G4UserStackingAction(){
    info = info_;
    } 

    
LabStackingAction::~LabStackingAction(){}


G4ClassificationOfNewTrack LabStackingAction::ClassifyNewTrack(const G4Track * aTrack){
  
//   if(aTrack->GetDefinition() == G4OpticalPhoton::OpticalPhotonDefinition()) {
//     ((G4Track*)aTrack)->SetTrackStatus(fStopAndKill);
//   }
  
  return fUrgent;
  
}

void LabStackingAction::NewStage(){}

void LabStackingAction::PrepareNewEvent(){}

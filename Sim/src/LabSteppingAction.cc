#include "LabSteppingAction.hh"

#include "G4Step.hh"
#include "G4Track.hh"
#include "G4OpticalPhoton.hh"

#include "G4Event.hh"
#include "G4SystemOfUnits.hh"
#include "G4RunManager.hh"
#include "G4SteppingManager.hh"
#include "G4SDManager.hh"
#include "G4EventManager.hh"
#include "G4ProcessManager.hh"
#include "G4Track.hh"
#include "G4Step.hh"
#include "G4Event.hh"
#include "G4StepPoint.hh"
#include "G4TrackStatus.hh"
#include "G4VPhysicalVolume.hh"
#include "G4ParticleDefinition.hh"
#include "G4ParticleTypes.hh"
#include "G4OpBoundaryProcess.hh"
#include "G4UnitsTable.hh"

#include <common.hh>

LabSteppingAction::LabSteppingAction(LabInfo *info_)
: G4UserSteppingAction(){ 
  
  info = info_;
}


LabSteppingAction::~LabSteppingAction(){}

void LabSteppingAction::UserSteppingAction(const G4Step* step){

  G4Track* track = step->GetTrack();
//   G4VPhysicalVolume *prePV  = step->GetPreStepPoint()->GetPhysicalVolume();
  G4VPhysicalVolume *postPV = step->GetPostStepPoint()->GetPhysicalVolume();
  
   if(!postPV){//out of world (to avoid segmentation fault)
        return;
    }
 

  
  // All of the following is to save information on the detected optical photons
  // Check if in the last Geant4 release this has been improved
  G4OpBoundaryProcessStatus boundaryStatus=Undefined;
  static G4ThreadLocal G4OpBoundaryProcess* boundary = NULL;

  //find the boundary process only once
  if(!boundary){
    G4ProcessManager* pm = step->GetTrack()->GetDefinition()->GetProcessManager();
    G4int nprocesses = pm->GetProcessListLength();
    G4ProcessVector* pv = pm->GetProcessList();
    G4int i;
    for( i=0;i<nprocesses;i++){
      if((*pv)[i]->GetProcessName()=="OpBoundary"){
        boundary = (G4OpBoundaryProcess*)(*pv)[i];
        break;
      }
    }
  }
  
  if(track->GetDefinition() == G4OpticalPhoton::OpticalPhotonDefinition()) { // if optical photon
      
    G4StepPoint* thePostPoint = step->GetPostStepPoint();
      //((G4Track*)track)->SetTrackStatus(fStopAndKill); 
    
    if(!(step->GetPostStepPoint()->GetPhysicalVolume())){//out of world
        return;
    }
    
    G4String thePrePV  = step->GetPreStepPoint()->GetPhysicalVolume()->GetName();
    G4String thePostPV = step->GetPostStepPoint()->GetPhysicalVolume()->GetName();
   
    if(thePostPoint->GetStepStatus() == fGeomBoundary){ // if at boundary
        
      boundaryStatus = boundary->GetStatus();
      
      /* Count detected photons */
      switch(boundaryStatus){
      case Absorption: // absorption at every boundary
        info->Absorption++;
        break;
      case Detection:{	// if the status is detection, the photon is entering the SiPM
        
        G4double time = step->GetPostStepPoint()->GetGlobalTime();
        G4double pos[3];
        pos[0] = track->GetPosition().x();
        pos[1] = track->GetPosition().y();
        pos[2] = track->GetPosition().z();

        if (thePrePV=="Grease1" && thePostPV=="SiPM1"){
            // append to detection_vector the current info
              detection_vector1.push_back(  detection(float(info->event_id), track->GetKineticEnergy()/eV, time/ns, pos[0]/mm, pos[1]/mm));
              info->Detection1++;
        } 
        else if (thePrePV=="Grease2" && thePostPV=="SiPM2"){
            // append to detection_vector the current info
              detection_vector2.push_back(  detection(float(info->event_id), track->GetKineticEnergy()/eV, time/ns, pos[0]/mm, pos[1]/mm));
              info->Detection2++;
        } 
        if (thePrePV=="Grease3" && thePostPV=="SiPM3"){
            // append to detection_vector the current info
              detection_vector3.push_back(  detection(float(info->event_id), track->GetKineticEnergy()/eV, time/ns, pos[0]/mm, pos[1]/mm));
              info->Detection3++;
        } 
        else if (thePrePV=="Grease4" && thePostPV=="SiPM4"){
            // append to detection_vector the current info
              detection_vector4.push_back(  detection(float(info->event_id), track->GetKineticEnergy()/eV, time/ns, pos[0]/mm, pos[1]/mm));
              info->Detection4++;
        } 
        
        else{
            G4cout << G4endl;
            G4cout << "WARNING by SteppingAction: detection occurring outside SiPM!" << G4endl; 
            exit(EXIT_FAILURE);
        }
        
      } break;// end of case Detection
      case FresnelRefraction:
        info->FresnelRefraction++;
            break;
      
      case FresnelReflection:
        info->FresnelReflection++;
            break;
      
      case TotalInternalReflection:
        info->TotalInternalReflection++;
            break;
      
      case LambertianReflection:
        info->LambertianReflection++;
            break;
      
      case LobeReflection:
        info->LobeReflection++;
            break;
      
      case SpikeReflection:
        info->SpikeReflection++;
            break;
      
      case BackScattering:
        info->BackScattering++;
            break;
      
      case NotAtBoundary:
        info->NotAtBoundary++;
            break;
      
      case SameMaterial:
        info->SameMaterial++;
            break;
      
      case StepTooSmall:
        //info->StepTooSmall++;
            break;
      
      case NoRINDEX:
        info->NoRINDEX++;
            break;
      
      default: 
//         G4cout << boundaryStatus << G4endl;
    //for debug
//              FILE* PhotonsSipm;
//              PhotonsSipm = fopen("Interfaces.txt","a");
//              fprintf(PhotonsSipm, "%d %d %4.2f %4.2f %4.2f\n", info->event_id, track->GetTrackID(), track->GetPosition().x()/mm, track->GetPosition().y()/mm, track->GetPosition().z()/mm);
//              fclose(PhotonsSipm);
        break;
  
    } /* end of switch */
   }  /* end of if at boundary */
  }   /* end of if optical photon */

  
} /* end of void*/


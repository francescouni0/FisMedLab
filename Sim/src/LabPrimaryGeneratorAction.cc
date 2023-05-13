#include "LabPrimaryGeneratorAction.hh"
#include "Randomize.hh"

#include "G4Event.hh"
// #include "G4ParticleGun.hh"
#include "G4GeneralParticleSource.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "G4SystemOfUnits.hh"
#include "G4ParticleGun.hh"


//when finished with Na22, delete the 1 and comment the creation o fParticleGun1
LabPrimaryGeneratorAction::LabPrimaryGeneratorAction(LabInfo *info_)
 : G4VUserPrimaryGeneratorAction(), fParticleGun(0){
  
  info = info_;
  fParticleGun = new G4GeneralParticleSource();

//  G4ParticleTable *particleTable = G4ParticleTable::GetParticleTable();
//  G4ParticleDefinition *particle = particleTable->FindParticle("geantino");
//
//  G4ThreeVector pos (0.,  0.,  0. );
//  G4ThreeVector mom (0. , 1. , 0. );
//   
//  fParticleGun->SetParticlePosition(pos);
//  fParticleGun->SetParticleMomentumDirection(mom);
//  fParticleGun->SetParticleMomentum(0*GeV);
//  fParticleGun->SetParticleDefinition(particle);

}

LabPrimaryGeneratorAction::~LabPrimaryGeneratorAction(){
  delete fParticleGun;
//   delete fGunMessenger;
}

void LabPrimaryGeneratorAction::GeneratePrimaries(G4Event* anEvent){

   // G4ParticleDefinition *particle = fParticleGun1->GetParticleDefinition();
//
   // if(particle == G4Geantino::Geantino())
   // {
   //   G4int Z= 11;
   //   G4int A= 22;
//
   //   G4double charge   = 0.*eplus;
   //   G4double excitEnergy = 0.*keV;
//
   //   G4ParticleDefinition *ion = G4IonTable::GetIonTable()->GetIon(Z,A,excitEnergy);
//
   //   fParticleGun1->SetParticleDefinition(ion);
   //   fParticleGun1->SetParticleCharge(charge);
   // }




  
  // //Set primary particle parameters  
  // G4ParticleTable* particleTable = G4ParticleTable::GetParticleTable();
  // G4ParticleDefinition* particle = particleTable->FindParticle(info->particleName);
  // fParticleGun->SetParticleDefinition(particle);
  // fParticleGun->SetParticleTime(0.0*ns);
  // fParticleGun->SetParticlePosition(G4ThreeVector(info->beamPos[0]*mm,info->beamPos[1]*mm, info->beamPos[2]*mm));
  // fParticleGun->SetParticleMomentumDirection(G4ThreeVector(info->beamDirection[0], info->beamDirection[1], info->beamDirection[2]));
  // fParticleGun->SetParticleEnergy(info->beamEnergy*eV);
  //
  //if (fParticleGun->GetParticleDefinition()->GetParticleName()=="geantino"){
  //    G4ThreeVector normal (0., 0., 1.);
  //    G4ThreeVector kphoton = fParticleGun->GetParticleMomentumDirection();
  //    G4ThreeVector product = normal.cross(kphoton);
  //    G4double modul2       = product*product;
//
  //    G4ThreeVector e_perpend (0., 0., 1.);
  //    if (modul2 > 0.) e_perpend = (1./std::sqrt(modul2))*product;
  //    G4ThreeVector e_paralle    = e_perpend.cross(kphoton);
  //    
  //    G4double angle = G4UniformRand() * 360.0*deg;
  //    G4ThreeVector polar = std::cos(angle)*e_paralle + std::sin(angle)*e_perpend;
  //    fParticleGun->SetParticlePolarization(polar);
  // }

  fParticleGun->GeneratePrimaryVertex(anEvent);
  info->event_id++;
  if(info->numOfEvents>=100){
     G4int percent=info->event_id/(info->numOfEvents/100);
     if(info->event_id%(info->numOfEvents/100) == 0){ // %
    	G4cout << percent << "%" << G4endl;
     }
  }
  // for output
  info->particleName = fParticleGun->GetParticleDefinition()->GetParticleName();
  info->beamEnergy   = fParticleGun->GetParticleEnergy()/keV;
  info->beamPos[0]   = fParticleGun->GetParticlePosition().x()/mm;
  info->beamPos[1]   = fParticleGun->GetParticlePosition().y()/mm;
  info->beamPos[2]   = fParticleGun->GetParticlePosition().z()/mm;
  info->beamDirection[0]   = fParticleGun->GetParticleMomentumDirection().x();
  info->beamDirection[1]   = fParticleGun->GetParticleMomentumDirection().y();
  info->beamDirection[2]   = fParticleGun->GetParticleMomentumDirection().z();

}


#ifndef LabPrimaryGeneratorAction_h
#define LabPrimaryGeneratorAction_h 1

#include "G4VUserPrimaryGeneratorAction.hh"
#include "globals.hh"
#include "LabInfo.hh"
#include "G4IonTable.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "G4Geantino.hh"
#include "G4ParticleGun.hh"

class G4ParticleGun;
class G4GeneralParticleSource;
class G4Event;
class LabPrimaryGeneratorMessenger;


class LabPrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{
  public:
    LabPrimaryGeneratorAction(LabInfo* info);
    virtual ~LabPrimaryGeneratorAction();

  public:
    virtual void GeneratePrimaries(G4Event*);

    void SetOptPhotonPolar();
    void SetOptPhotonPolar(G4double);

  private:
    G4GeneralParticleSource* fParticleGun;
    G4ParticleGun* fParticleGun1;
//     LabPrimaryGeneratorMessenger* fGunMessenger;
    LabInfo *info; 
};

#endif /*LabPrimaryGeneratorAction_h*/

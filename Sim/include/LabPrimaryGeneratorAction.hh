
#ifndef LabPrimaryGeneratorAction_h
#define LabPrimaryGeneratorAction_h 1

#include "G4VUserPrimaryGeneratorAction.hh"
#include "globals.hh"
#include "LabInfo.hh"

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
//     LabPrimaryGeneratorMessenger* fGunMessenger;
    LabInfo *info; 
};

#endif /*LabPrimaryGeneratorAction_h*/

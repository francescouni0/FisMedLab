
#ifndef LabStackingAction_H
#define LabStackingAction_H 1

#include "globals.hh"
#include "G4UserStackingAction.hh"
#include "LabInfo.hh" 


class LabStackingAction : public G4UserStackingAction
{
  public:
    LabStackingAction(LabInfo* info);  
    virtual ~LabStackingAction();

  public:
    virtual G4ClassificationOfNewTrack ClassifyNewTrack(const G4Track* aTrack);
    virtual void NewStage();
    virtual void PrepareNewEvent();

  private:
    G4int fScintillationCounter;
    G4int fCerenkovCounter;
    
    LabInfo *info; 
};

#endif

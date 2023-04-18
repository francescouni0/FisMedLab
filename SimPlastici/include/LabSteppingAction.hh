
// $Id: LabSteppingAction.hh 69469 2013-05-05 21:42:35Z ihrivnac $
//
/// \file LabSteppingAction.hh
/// \brief Definition of the LabSteppingAction class

#ifndef LabSteppingAction_h
#define LabSteppingAction_h 1

#include "G4UserSteppingAction.hh"
#include "globals.hh"
#include "G4OpBoundaryProcess.hh"
#include "LabInfo.hh" 



class LabSteppingAction : public G4UserSteppingAction
{
  public:
    LabSteppingAction(LabInfo* info);  
    virtual ~LabSteppingAction();

    // method from the base class
    virtual void UserSteppingAction(const G4Step*);

  private:
    G4int fScintillationCounter;
    G4int fCerenkovCounter;
    G4int fEventNumber;

    G4OpBoundaryProcessStatus fExpectedNextStatus;
    
    LabInfo *info; 
};

#endif


#ifndef LabRunAction_h
#define LabRunAction_h 1

#include "globals.hh"
#include "G4UserRunAction.hh"
#include "LabInfo.hh" 


class G4Timer;
class G4Run;

class LabRunAction : public G4UserRunAction
{
  public:
    LabRunAction(LabInfo* info);
    virtual ~LabRunAction();

  public:
    virtual void BeginOfRunAction(const G4Run* aRun);
    virtual void EndOfRunAction(const G4Run* aRun);

  private:
    G4Timer* fTimer;
    LabInfo *info;
};


#endif /*LabRunAction_h*/


class LabSteppingVerbose;

#ifndef LabSteppingVerbose_h
#define LabSteppingVerbose_h 1

#include "G4SteppingVerbose.hh"



class LabSteppingVerbose : public G4SteppingVerbose
{
 public:

   LabSteppingVerbose();
   virtual ~LabSteppingVerbose();

   virtual void StepInfo();
   virtual void TrackingStarted();

};



#endif

// $Id: LabActionInitialization.hh 68058 2013-03-13 14:47:43Z gcosmo $

/// \file LabActionInitialization.hh
/// \brief Definition of the LabActionInitialization class

#ifndef LabActionInitialization_h
#define LabActionInitialization_h 1

#include "G4VUserActionInitialization.hh"
#include "LabInfo.hh"

class B4DetectorConstruction;

// Action initialization class.

class LabActionInitialization : public G4VUserActionInitialization
{
  public:
    LabActionInitialization(LabInfo* info);  
    virtual ~LabActionInitialization();

    virtual void BuildForMaster() const;
    virtual void Build() const;

    virtual G4VSteppingVerbose* InitializeSteppingVerbose() const;
    
  private:
    LabInfo *info; 
};

#endif


#include <stdlib.h>
#include <math.h>

#include "G4ios.hh"
#include "G4SystemOfUnits.hh"
#include "LabInfo.hh"


LabInfo::LabInfo(){}

LabInfo::~LabInfo(){}


void LabInfo::dump() {

    // A summary of the simulation run parameters is saved into 'simulationSummary.txt' along with the simulation output in out.raw

    FILE* fileInfo;
    fileInfo = fopen(summaryFileName,"wr");
    
    // beam info
    fprintf(fileInfo, "Information on the primary beam:\n");
    fprintf(fileInfo, "number of simulated events: %d\n",  numOfEvents);
    fprintf(fileInfo, "type of particle: %s\n",  particleName.c_str());
    fprintf(fileInfo, "beam energy: %3.3f keV\n",  beamEnergy);
    fprintf(fileInfo, "beam position: %2.2f mm, %2.2f mm, %2.2f mm\n",  beamPos[0],  beamPos[1], beamPos[2]);
    fprintf(fileInfo, "beam direction: %2.2f, %2.2f, %2.2f \n",  beamDirection[0],  beamDirection[1], beamDirection[2]);
    fprintf(fileInfo, "\n");
    
    fprintf(fileInfo, "World dimensions: %2.2f m, %2.2f m, %2.2f m \n",  worldSize[0],  worldSize[1], worldSize[2]);
    fprintf(fileInfo, "Scintillator dimensions: %4.2f mm, %4.2f mm, %4.2f mm\n",  scintSize[0],  scintSize[1], scintSize[2]);
    fprintf(fileInfo, "Scintillator position: %2.2f mm, %2.2f mm, %2.2f mm\n",  scintPos[0],  scintPos[1], scintPos[2]);
    fprintf(fileInfo, "Grease thickness: %4.2f um\n",  greaseThickness);
    fprintf(fileInfo, "Wrapping reflectivity: %2.4f\n",  reflectivityLateral);
    fprintf(fileInfo, "\n");

    fprintf(fileInfo, "Optical interfaces:\n");
    fprintf(fileInfo, "scintToGreaseType: %s, scintToGreaseModel: %s, scintToGreaseModel: %s \n",  scintToGreaseType.c_str(), scintToGreaseModel.c_str(), scintToGreaseFinish.c_str());
    fprintf(fileInfo, "greaseToScintType: %s, greaseToScintModel: %s, greaseToScintFinish: %s \n",  greaseToScintType.c_str(), greaseToScintModel.c_str(), greaseToScintFinish.c_str());
    fprintf(fileInfo, "greaseToSiPMType: %s, greaseToSiPMModel: %s, greaseToSiPMFinish: %s \n",  greaseToSiPMType.c_str(), greaseToSiPMModel.c_str(), greaseToSiPMFinish.c_str());
    fprintf(fileInfo, "\n");
    

    // header for output files
    fprintf(fileInfo, "Output files headers:\n");
    fprintf(fileInfo, "detectN_PosZ.raw:\n");
    fprintf(fileInfo, "detection(float(info->event_id), track->GetKineticEnergy()/eV, time/ns, pos[0]/mm, pos[1]/mm)\n");
    fprintf(fileInfo, "\n");
    
    // simulation seed
    fprintf(fileInfo, "Simulation seed: %d\n", seed);
    fprintf(fileInfo, "\n");
  
    
    // timer info
    fprintf(fileInfo, "timers (s): %f (real), %f (system), %f (user)\n", timer[0]/s, timer[1]/s, timer[2]);
 
    fclose(fileInfo);

}

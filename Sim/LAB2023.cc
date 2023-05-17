// Starting example: OpNovice (various G4 versions)
// Note: due to the use of CMake globbing to create the source file list, if you add or remove files (i.e. project classes), you must remember to rerun CMake to pick up the changes.

#include "G4SystemOfUnits.hh"
#include "QGSP_BERT.hh"
#include "G4OpticalPhysics.hh"
#include "G4EmStandardPhysics_option4.hh"
#include "G4StepLimiterPhysics.hh"
#include "G4RunManager.hh"
#include "G4MTRunManager.hh"
#include "G4UnitsTable.hh"

#include "G4UImanager.hh"
#include "G4VisExecutive.hh"
#include "G4UIExecutive.hh"

#include "LabInfo.hh"
#include "LabDetectorConstruction.hh"
#include "LabActionInitialization.hh"
// global variable to write output
#include <common.hh>
 
// concurrent vector to write output in multithread mode without conflicts 
// currently multithread not active
tbb::concurrent_vector<detection> detection_vector1;
tbb::concurrent_vector<detection> detection_vector2;

namespace {

  void PrintUsage() {
    G4cerr << " Usage: " << G4endl;
    G4cerr << " Lab [-m macro ] [-r seed] "  << G4endl;
//     G4cerr << " Lab [-m macro ] [-u UIsession] [-t nThreads] [-r seed] "  << G4endl;
//     G4cerr << " Lab [-t nThreads] [-r seed] "  << G4endl;
//     G4cerr << "   note: -t option is available only for multi-threaded mode." << G4endl;
  }
}



int main(int argc, char** argv) {
    
  // Evaluate arguments
  if ( argc > 5 ) {
    PrintUsage();
    return 1;
  }
  
  // Detect interactive mode (if no arguments) and define UI session
  G4UIExecutive* ui = 0;
  if ( argc == 1 ) {
    ui = new G4UIExecutive(argc, argv);
  }
  
  G4String macro;
  G4String session;

  G4int nThreads = 2;

  for ( G4int i=1; i<argc; i=i+2 ) {
    if      ( G4String(argv[i]) == "-m" ) macro   = argv[i+1];
   // else if ( G4String(argv[i]) == "-r" ) info->seed  = atoi(argv[i+1]);
// #ifdef G4MULTITHREADED
//     else if ( G4String(argv[i]) == "-t" ) {
// 		    nThreads = G4UIcommand::ConvertToInt(argv[i+1]);
//     }
// #endif
    else {
      PrintUsage();
      return 1;
    }
}

  // Choose the Random engine
  G4Random::setTheEngine(new CLHEP::RanecuEngine);

  G4RunManager * runManager = new G4RunManager;
  
  //G4MTRunManager * runManager = new G4MTRunManager;
  runManager->SetNumberOfThreads(nThreads);
  
  
    /* get all information */
    LabInfo *info = NULL;
    if((info = new LabInfo()) == NULL ) {
        G4cerr << "Impossible to create LabInfo" << G4endl;
    }
    
    // ****************************************************************
    //
    //                Set simulation parameters here    
    // 
    // ****************************************************************
    
    info->seed                = (G4int)time(0); // use fixed seed for tests (e.g. 0), random number for simulation, e.g. (G4int)time(0);
    info->optPhysVerb         = 0;  // verbosity level of optical photons physics (0 -> 1)
    //info->verbose             = 2;   // global verbose level (0 -> 2), overidden by macro if given
    info->stepLimiter         = 100.0*um; // to be changed
    
    // World dimensions
    info->worldSize[0]        = 1000.0; // mm
    info->worldSize[1]        = 1000.0; // mm
    info->worldSize[2]        = 1000.0; // mm
    
    // Scintillator dimensions
    info->scintSize[0]        =  20.0; // mm
    info->scintSize[1]        =   3.0; // mm scintillator thickness
    info->scintSize[2]        = 440.0; // mm bar length
    
    // Position of scintillator in the world volume
    info->scintPos[0] 	      =  0.0; // mm
    info->scintPos[1]         =  0.0; // mm
    info->scintPos[2]         =  0.0; // mm
    
    // Optical grease thickness
    info->greaseThickness     = 1000; // um
    
    // Energy range to simulate, optical properties of all materials should be defined in this range
    info->enRange[0]          = 1.90; // eV
    info->enRange[1]          = 3.31; // eV

    // Otical interfaces
    // Wrapping
    info->reflectivityLateral = 0.99; // to be tuned <---------------
    info->scintToLateralWrappingType   = "dielectric_metal";
    info->scintToLateralWrappingModel  = "unified";
    info->scintToLateralWrappingFinish = "polished";

    // Scint -> Grease
    info->scintToGreaseType   = "dielectric_dielectric";
    info->scintToGreaseModel  = "unified";
    info->scintToGreaseFinish = "polished";

    // Grease -> Scint
    info->greaseToScintType   = "dielectric_dielectric";
    info->greaseToScintModel  = "unified";
    info->greaseToScintFinish = "polished";

    // Grease -> SiPM
    info->greaseToSiPMType   = "dielectric_dielectric";
    info->greaseToSiPMModel  = "unified";
    info->greaseToSiPMFinish = "polished";    
    
    // Primary beam settings
    info->numOfEvents         = 10000;                          // number of primary particles to generate
 
 
    // ****************************************************************
    //
    //                      End of settings    
    // 
    // ****************************************************************
    
      
  
  // Seed the random number generator manually
  G4Random::setTheSeed(info->seed);

  // Set mandatory initialization classes
  
  // Detector construction
  runManager-> SetUserInitialization(new LabDetectorConstruction(info));

  // Physics list
  G4VModularPhysicsList* physicsList = new QGSP_BERT;
  physicsList->RegisterPhysics(new G4StepLimiterPhysics()); // add step limiter
  physicsList->ReplacePhysics(new G4EmStandardPhysics_option4()); // replace EM physics option (try option3 and option4)
  //physicsList->ReplacePhysics(new G4EmLivermorePhysics()); // replace EM physics with Livermore
  physicsList->RegisterPhysics(new G4OpticalPhysics(info->optPhysVerb)); // add optical physics to list
  runManager->SetUserInitialization(physicsList);
  // options 3 and 4 are more accurate than 1 and 2 for low energy
  // they have the same models for gammas
  // for electrons, option4 is the most accurate because it includes single coulomb scattering, and the models for msc are different in opt3 and 4
  
  // User action initialization
  runManager->SetUserInitialization(new LabActionInitialization(info)); 
  
  // Initialize visualization
  // G4VisExecutive can take a verbosity argument - see /vis/verbose guidance.
  G4VisManager* visManager = new G4VisExecutive("Quiet");
  visManager->Initialize();
  
  // Initialize G4 kernel
  runManager->Initialize();

  // Get the pointer to the User Interface manager
  G4UImanager* UImanager = G4UImanager::GetUIpointer(); 
  
//   if(info->verbose == 1){
//     UImanager->ApplyCommand("/tracking/verbose 1");
//   }else if(info->verbose == 2){
//     UImanager->ApplyCommand("/tracking/verbose 2");
//   }
  
  
  if (macro.size()) {

      G4cout << "Executing macro..." <<  G4endl;
      // Batch mode
      G4String command = "/control/execute ";
      UImanager->ApplyCommand(command+macro);
  }
  else{
    // interactive mode
    UImanager->ApplyCommand("/control/execute init_vis.mac");
    ui->SessionStart();
    delete ui;
  }
  
  G4String posList[] = {"-200.0","-160.0","-120.0","-80.0","-40.0","0.0","40.0","80.0","120.0","160.0","200.0"};
  //G4String posList[] = {"-180.0", "180.0"};
  G4int numPos = sizeof(posList)/sizeof(G4String);
  
  for (int currPos = 0; currPos < numPos; currPos++){
    
    G4cout << "beam position: " << posList[currPos] << " mm" << G4endl;
    UImanager->ApplyCommand("/gps/position   0.0 -25.0 "+posList[currPos]+" mm");
    
    // clears output vectors before run
    detection_vector1.clear();         
    detection_vector2.clear();  
    
    info->summaryFileName = "./info.txt";
  
  // clears output file before run
    FILE* fileInfo = NULL;
      if((fileInfo = fopen(info->summaryFileName,"wr")) == NULL) {
        G4cout << "Impossible to open the file " << info->summaryFileName << " for writing" << G4endl;
      }
      if((fclose(fileInfo)) == EOF) {
        G4cerr << "Impossible to close the file " << info->summaryFileName << G4endl;
      }
  
    info->event_id = 0; // updated in PrimaryGeneratorAction to return event number
    info->Detection1 = 0;       
    info->Detection2 = 0;       
  
    runManager->BeamOn(info->numOfEvents); // runs simulation

  // Write results to output
    
    std::ofstream file_out2("./detect1_2mm"+posList[currPos]+".raw");
    for (uint32_t i=0; i<detection_vector1.size(); i++) {
      file_out2.write(reinterpret_cast<char*>(&detection_vector1[i]), sizeof(detection));
    }
    file_out2.close();
  
    std::ofstream file_out3("./detect2_25mm"+posList[currPos]+".raw");
    for (uint32_t i=0; i<detection_vector2.size(); i++) {
      file_out3.write(reinterpret_cast<char*>(&detection_vector2[i]), sizeof(detection));
    }
    file_out3.close();
    
    info->dump();
    
     // Print out some particle counters at the end of the simulation
      G4cout << G4endl;
      G4cout << "Detection1:              " << info->Detection1 << G4endl;
      G4cout << "Detection2:              " << info->Detection2 << G4endl;
      G4cout << G4endl;
  
    // Job termination
    // Free the store: user actions, physics_list and detector_description are
    //                 owned and deleted by the run manager, so they should not
    //                 be deleted in the main() program !
  }

  delete visManager;

  delete runManager;

  return 0;
}



const header = {
  homepage: '/',
  title: 'Home',
}

const about = {
  name: 'Aisw@riya',
  role: 'Data Scientist',
  description:
    'in-times I Make Computers Think !',
  social: {
    linkedin: 'https://www.linkedin.com/in/aiswariya-a-v-a38800210',
    github: 'https://github.com/aiswariya2324',
  },
}

const projects = [
  {
    name: 'T-BOT',
    description:
      `Creating a user-friendly interface for people to access in their
      own regional languages for better understanding using a
      voice bot regarding any queries they have. The A.I.
      can identify and give responses in regional languages so
      that even illiterates and tourists and other public people can
      understand.`,
    stack: ['TensorFlow', 'IoT', 'ReactJS'],
  },
  {
    name: 'Project 2',
    description:
      `Aggregate web-app that 
      contains all the details of doctors in a specific locality which enables the user to fix 
      appointments with them online. The web app would basically have an AI chatbot that can 
      aid in predicting and diagnosing a disease and recommending medication tips for that 
      particular disease. It also provides the details of available doctors who are specialised in 
      treating that particular disease and fixes appointment with our desired doctor.`,
    stack: ['TensorFlow', 'IoT', 'React Native'],
  },
  {
    name: 'Project 3',
    description:
      `Employing CCTV in public spaces to spot stray dog behaviour 
      patterns, skin conditions they are prone to, and to count the number of stray dogs that 
      are in the region. We gathered normal and multispectral images of several skin diseases 
      in dogs in order to develop a classification model for their skin conditions.
      The single models and consensus models were created using the CNN model architectures 
      InceptionNet, ResNet, DenseNet, and MobileNet. We provide the Animal Welfare Board with 
      pertinent information in order for them to address the problem by moving it to a location 
      where they are responsible for the welfare of dogs because there are many chances for 
      problems to arise when the number of dogs in a region increases rapidly.`,
    stack: ['PyTorch', 'IoT', 'ReactJS'],
    sourceCode: 'https://github.com',
    livePreview: 'https://github.com',
  },
]

const skills = [
  'HTML',
  'CSS',
  'ReactJS',
  'TensorFlow',
  'Keras',
  'NumPy',
  'Pandas',
  'Computer Vision',
  'Git',
  'PyTorch',
  'Bash',
  'Selenium',
]

const contact = {
  email: 'aiswariya2324@gmail.com',
}

export { header, about, skills, projects, contact }

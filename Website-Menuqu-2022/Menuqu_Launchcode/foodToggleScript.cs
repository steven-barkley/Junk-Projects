using UnityEngine;
using System.Collections;
using Vuforia;

public class foodToggleScript : MonoBehaviour, IVirtualButtonEventHandler {

    public GameObject[] menuItems = new GameObject[9];

    private GameObject menuItem;

    private GameObject vbButtonObject;

    //// Use this for initialization
    int i = 0;
    /// </summary>
    void Start()
    {
        vbButtonObject = GameObject.Find("actionButton");
        menuItem = GameObject.Find(menuItems[i].name);
        vbButtonObject.GetComponent<VirtualButtonBehaviour>().RegisterEventHandler(this);
        //SetActive of all to false

        menuItems[i].SetActive(false);
        menuItems[i + 1].SetActive(false);
        menuItems[i + 2].SetActive(false);
        menuItems[i + 3].SetActive(false);
        menuItems[i + 4].SetActive(false);
        menuItems[i + 5].SetActive(false);
        menuItems[i + 6].SetActive(false);
        menuItems[i + 7].SetActive(false);
        menuItems[i + 8].SetActive(false);
    }
    public void OnButtonPressed(VirtualButtonAbstractBehaviour vb)
    {
        Debug.Log("button down");
        Debug.Log(i);
        menuItems[i].SetActive(true);//was true
    }
    public void OnButtonReleased(VirtualButtonAbstractBehaviour vb)
    {
        if (i<=7)
        {
            Debug.Log("button up");
            menuItems[i].SetActive(false);//was false
            IncreaseVariable(menuItem);
            menuItems[i].SetActive(true);//Changed line
        }
    }
    void IncreaseVariable(GameObject j)
    {
        if (i<7)
        {
            i++;
        }
        else if (i>=7)
        {
            i = i - 7;
        }
    }
}

